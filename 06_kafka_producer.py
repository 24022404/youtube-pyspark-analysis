"""
06_kafka_producer.py
Kafka Producer - CRAWL REAL-TIME từ YouTube API
"""
import os
from kafka import KafkaProducer
from googleapiclient.discovery import build
import json
import time
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# YOUTUBE API KEY
API_KEY = 'AIzaSyBHZ-BVjZUVWMxhJfJ3k85PdQh12Hyf70k'

class YouTubeKafkaProducer:
    def __init__(self, bootstrap_servers= None, topic='youtube-trending'):
        
        if bootstrap_servers is None:
            bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

        self.topic = topic
        # Kafka Producer
        try:
            self.producer = KafkaProducer(
                bootstrap_servers=bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                acks='all',
                retries=3
            )
            logger.info(f"✅ Kafka Producer connected to {bootstrap_servers}")
        except Exception as e:
            logger.error(f"❌ Cannot connect to Kafka: {e}")
            raise
        
        # YouTube API
        try:
            self.youtube = build('youtube', 'v3', developerKey=API_KEY)
            logger.info("✅ YouTube API initialized")
        except Exception as e:
            logger.error(f"❌ Cannot initialize YouTube API: {e}")
            raise
    
    def crawl_trending_videos(self, region_code='US', max_results=50):
        """Crawl trending videos từ YouTube"""
        try:
            request = self.youtube.videos().list(
                part='snippet,statistics',
                chart='mostPopular',
                regionCode=region_code,
                maxResults=max_results
            )
            response = request.execute()
            
            videos = []
            trending_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            
            for item in response['items']:
                snippet = item['snippet']
                stats = item['statistics']
                
                video = {
                    'video_id': item['id'],
                    'title': snippet['title'],
                    'publishedAt': snippet['publishedAt'],
                    'channelId': snippet['channelId'],
                    'channelTitle': snippet['channelTitle'],
                    'categoryId': int(snippet['categoryId']),
                    'trending_date': trending_date,
                    'tags': '|'.join(snippet.get('tags', [])),
                    'view_count': int(stats.get('viewCount', 0)),
                    'likes': int(stats.get('likeCount', 0)),
                    'dislikes': 0,
                    'comment_count': int(stats.get('commentCount', 0)),
                    'thumbnail_link': snippet['thumbnails']['default']['url'],
                    'comments_disabled': 'commentCount' not in stats,
                    'ratings_disabled': False,
                    'description': snippet['description'],
                    'kafka_timestamp': datetime.now().isoformat()
                }
                videos.append(video)
            
            logger.info(f"📊 Crawled {len(videos)} trending videos")
            return videos
            
        except Exception as e:
            logger.error(f"❌ Error crawling YouTube: {e}")
            return []
    
    def stream_realtime(self, interval=600, batch_size=10):
        """
        Stream real-time data từ YouTube
        
        Args:
            interval: Thời gian giữa các lần crawl (giây) - Mặc định 10 phút
            batch_size: Số video gửi mỗi lần
        """
        logger.info(f"🚀 REAL-TIME STREAMING STARTED")
        logger.info(f"   Crawl interval: {interval}s ({interval/60:.0f} minutes)")
        logger.info(f"   Batch size: {batch_size}")
        
        count = 0
        
        try:
            while True:
                # Crawl YouTube
                videos = self.crawl_trending_videos(max_results=50)
                
                if not videos:
                    logger.warning("⚠️ No videos crawled, retrying in 60s...")
                    time.sleep(60)
                    continue
                
                # Gửi vào Kafka theo batch
                for i, video in enumerate(videos):
                    try:
                        future = self.producer.send(self.topic, value=video)
                        future.get(timeout=10)
                        count += 1
                        
                        # Log mỗi batch
                        if (i + 1) % batch_size == 0:
                            logger.info(
                                f"📤 Sent {i+1}/{len(videos)} videos | "
                                f"Total: {count} | "
                                f"Latest: {video['title'][:40]}..."
                            )
                    
                    except Exception as e:
                        logger.error(f"❌ Error sending video: {e}")
                
                self.producer.flush()
                logger.info(f"✅ Batch completed! Total sent: {count} videos")
                logger.info(f"⏳ Waiting {interval}s until next crawl...")
                time.sleep(interval)
        
        except KeyboardInterrupt:
            logger.warning(f"⚠️ Stopped! Total sent: {count} videos")
        except Exception as e:
            logger.error(f"❌ Error: {e}")
        finally:
            self.close()
    
    def close(self):
        """Đóng Kafka Producer"""
        if self.producer:
            self.producer.close()
            logger.info("👋 Kafka Producer closed")


def main():
    print("=" * 70)
    print("KAFKA PRODUCER - YOUTUBE REAL-TIME CRAWLER")
    print("=" * 70)
    
    producer = YouTubeKafkaProducer(
        # bootstrap_servers='localhost:9092',
        topic='youtube-trending'
    )
    
    # Stream real-time với crawl mỗi 10 phút
    producer.stream_realtime(interval=60, batch_size=10)


if __name__ == "__main__":
    main()