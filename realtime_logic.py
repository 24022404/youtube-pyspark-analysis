# ========================================
# IMPORT LIBRARIES
# ========================================
import json
import time
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
import warnings
warnings.filterwarnings("ignore")

# ========================================
# GLOBAL SETTINGS
# ========================================
plt.style.use('dark_background')

CATEGORY_MAP = {
    '1': 'Film & Animation', '2': 'Autos & Vehicles', '10': 'Music',
    '15': 'Pets & Animals', '17': 'Sports', '19': 'Travel & Events',
    '20': 'Gaming', '22': 'People & Blogs', '23': 'Comedy',
    '24': 'Entertainment', '25': 'News & Politics', '26': 'Howto & Style',
    '27': 'Education', '28': 'Science & Technology', '29': 'Nonprofits & Activism'
}

# ========================================
# LOAD BASELINES
# ========================================
def load_baselines():
    baselines = {}
    for key in ['category', 'time', 'interaction']:
        path = f'./data/baselines/{key}_baseline.json'
        try:
            with open(path, 'r', encoding='utf-8') as f:
                baselines[key] = json.load(f)
        except FileNotFoundError:
            baselines[key] = None
    return baselines

baselines = load_baselines()

# ========================================
# INIT YOUTUBE API
# ========================================
API_KEY = 'AIzaSyBHZ-BVjZUVWMxhJfJ3k85PdQh12Hyf70k'  # Thay đổi nếu cần

try:
    youtube = build('youtube', 'v3', developerKey=API_KEY)
except Exception:
    youtube = None

# ========================================
# FETCH CURRENT TRENDING
# ========================================
def get_current_trending(region_code='US', max_results=50):
    if youtube is None:
        return pd.DataFrame()

    try:
        request = youtube.videos().list(
            part='snippet,statistics',
            chart='mostPopular',
            regionCode=region_code,
            maxResults=max_results
        )
        response = request.execute()

        videos = []
        for item in response.get('items', []):
            snippet = item['snippet']
            stats = item['statistics']
            published = datetime.strptime(snippet['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')

            videos.append({
                'video_id': item['id'],
                'title': snippet.get('title', ''),
                'channel': snippet.get('channelTitle', ''),
                'category_name': CATEGORY_MAP.get(snippet.get('categoryId', ''), 'Unknown'),
                'views': int(stats.get('viewCount', 0)),
                'likes': int(stats.get('likeCount', 0)),
                'comments': int(stats.get('commentCount', 0)),
                'published_at': published,
                'publish_hour': published.hour,
                'publish_day': published.strftime('%a'),
            })

        df = pd.DataFrame(videos)
        if not df.empty:
            df['like_rate'] = df['likes'] / df['views'] * 100
            df['comment_rate'] = df['comments'] / df['views'] * 100
            df['engagement_rate'] = (df['likes'] + df['comments']) / df['views'] * 100
        return df

    except Exception:
        return pd.DataFrame()

# ========================================
# CATEGORY / TIME / ENGAGEMENT COMPARISON
# ========================================
def compare_category(current_df, baseline):
    if current_df.empty or baseline is None:
        return None, []

    current_pct = (current_df['category_name'].value_counts(normalize=True) * 100).to_dict()
    baseline_pct = baseline['category_distribution']['by_percentage']

    comparison, anomalies = [], []
    for cat, base_val in baseline_pct.items():
        curr_val = current_pct.get(cat, 0)
        change_ratio = ((curr_val - base_val) / base_val * 100) if base_val > 0 else 0
        comparison.append({
            'category': cat,
            'baseline_%': base_val,
            'current_%': curr_val,
            'change_ratio': change_ratio
        })
        if abs(change_ratio) > 20:
            anomalies.append({'type': 'CATEGORY', 'category': cat,
                              'direction': 'SURGE' if change_ratio > 0 else 'DECLINE',
                              'change_ratio': change_ratio})
    return pd.DataFrame(comparison), anomalies


def compare_time_patterns(current_df, baseline):
    if current_df.empty or baseline is None:
        return None, []

    anomalies = []
    current_hourly = current_df['publish_hour'].value_counts().to_dict()
    baseline_hourly = baseline['hourly_distribution']['video_count_by_hour']

    for hour in range(24):
        curr = current_hourly.get(hour, 0)
        base = baseline_hourly.get(str(hour), 1)
        change_ratio = (curr - base) / base * 100
        if abs(change_ratio) > 50:
            anomalies.append({'type': 'TIME_HOUR', 'hour': hour, 'change_ratio': change_ratio})

    return current_hourly, anomalies


def compare_engagement(current_df, baseline):
    if current_df.empty or baseline is None:
        return None, []

    curr_eng = current_df['engagement_rate'].mean()
    base_eng = baseline['engagement_benchmarks']['avg_engagement_rate']
    change_ratio = (curr_eng - base_eng) / base_eng * 100

    anomalies = []
    if abs(change_ratio) > 20:
        anomalies.append({'type': 'ENGAGEMENT', 'change_ratio': change_ratio})

    return {'current': curr_eng, 'baseline': base_eng}, anomalies

# ========================================
# MONITORING FUNCTION (FOR DASHBOARD)
# ========================================
def continuous_monitoring(duration_minutes=2, interval_seconds=60):
    if youtube is None or not any(baselines.values()):
        return pd.DataFrame()

    end_time = datetime.now() + timedelta(minutes=duration_minutes)
    history = []

    while datetime.now() < end_time:
        df = get_current_trending()
        if df.empty:
            time.sleep(interval_seconds)
            continue

        all_anomalies = []
        if baselines['category']:
            _, cat_anom = compare_category(df, baselines['category'])
            all_anomalies.extend(cat_anom)
        if baselines['time']:
            _, time_anom = compare_time_patterns(df, baselines['time'])
            all_anomalies.extend(time_anom)
        if baselines['interaction']:
            _, eng_anom = compare_engagement(df, baselines['interaction'])
            all_anomalies.extend(eng_anom)

        history.append({
            'timestamp': datetime.now(),
            'videos_count': len(df),
            'anomalies_count': len(all_anomalies),
            'top_category': df['category_name'].mode()[0],
            'avg_engagement': df['engagement_rate'].mean()
        })
        time.sleep(interval_seconds)

    return pd.DataFrame(history)

# ========================================
# VISUALIZATION FUNCTION (RETURN FIG)
# ========================================
def plot_results(history_df):
    if history_df is None or history_df.empty:
        return None

    fig, axes = plt.subplots(2, 2, figsize=(16, 10))

    # Plot 1: Anomalies over time
    axes[0, 0].plot(history_df['timestamp'], history_df['anomalies_count'], marker='o')
    axes[0, 0].set_title('🚨 Anomalies Detected Over Time')

    # Plot 2: Top category frequency
    top_counts = history_df['top_category'].value_counts()
    axes[0, 1].bar(top_counts.index, top_counts.values)
    axes[0, 1].set_title('🏆 Most Frequent Top Categories')
    axes[0, 1].tick_params(axis='x', rotation=45)

    # Plot 3: Engagement over time
    axes[1, 0].plot(history_df['timestamp'], history_df['avg_engagement'], color='green', marker='s')
    axes[1, 0].set_title('💝 Average Engagement Over Time')

    # Plot 4: Summary table
    axes[1, 1].axis('off')
    summary = f"""
    Iterations: {len(history_df)}
    Total anomalies: {history_df['anomalies_count'].sum()}
    Avg engagement: {history_df['avg_engagement'].mean():.2f}%
    Most frequent top category: {history_df['top_category'].mode()[0]}
    """
    axes[1, 1].text(0.1, 0.5, summary, fontsize=12, family='monospace')

    plt.tight_layout()
    return fig
