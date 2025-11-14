import streamlit as st
from datetime import datetime
import realtime_logic

# =========================================================
# ⚙️ CẤU HÌNH TRANG CHÍNH
# =========================================================
st.set_page_config(
    page_title="BTL Big Data - Phân tích Dữ liệu YouTube",
    layout="wide",
    page_icon="📊"
)

# =========================================================
# 🧭 HEADER & GIỚI THIỆU
# =========================================================
st.title("📊 Dashboard Phân tích Dữ liệu YouTube Trending")
st.caption("Thực hiện bởi: Nhóm Big Data - Nhóm 08 | Cập nhật: " + datetime.now().strftime("%d/%m/%Y"))
st.divider()

# =========================================================
# 🎛️ THANH ĐIỀU HƯỚNG (SIDEBAR)
# =========================================================
st.sidebar.header("🔍 Chọn Chủ đề Phân tích")
main_topic = st.sidebar.radio(
    label="Chủ đề:",
    options=[
        "Phân tích Thể loại",
        "Phân tích Thời gian",
        "Phân tích Tương tác",
        "Giám sát Thời gian thực"
    ],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Mẹo: Chọn từng chủ đề để xem các biểu đồ và nhận xét tương ứng.")

# =========================================================
# 📂 HIỂN THỊ NỘI DUNG TƯƠNG ỨNG
# =========================================================

# ---------------------------------------------------------
# 🧩 PHÂN TÍCH 1: THỂ LOẠI
# ---------------------------------------------------------
if main_topic == "Phân tích Thể loại":
    st.header("🎬 Phân tích Thể loại (Category)")
    st.write("Phân tích độ phổ biến, tổng lượt xem, và số lượng kênh trong từng thể loại video YouTube.")

    st.subheader("1. Tần suất xuất hiện")
    st.image("images/category_analysis/01.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
     Phân tích đầu tiên cho thấy `Entertainment` (Giải trí) và `Gaming` (Trò chơi) là hai thể loại xuất hiện trên top trending thường xuyên nhất, theo sau là `Music` (Âm nhạc). Ba thể loại này chiếm phần lớn các video thịnh hành.
    """)

    st.divider()
    st.subheader("2. Tổng lượt xem")
    st.image("images/category_analysis/02.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    Mặc dù chỉ đứng thứ 3 về tần suất, `Music` lại dẫn đầu tuyệt đối về tổng lượt xem (36.1 tỷ), cho thấy các MV có sức hút khổng lồ. `Entertainment` theo sát với 33.0 tỷ lượt xem.
    """)

    st.divider()
    st.subheader("3. Độ đa dạng kênh")
    st.image("images/category_analysis/03.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    `Entertainment`, `Music`, và `Gaming` cũng là ba thể loại có số lượng kênh duy nhất tham gia trending nhiều nhất (trên 1,700 kênh mỗi loại), cho thấy đây là những "sân chơi" có tính cạnh tranh cao.
    """)
    
    st.divider()
    st.subheader("4. Mức độ tương tác")
    st.image("images/category_analysis/04.png",use_container_width=True)
    st.image("images/category_analysis/04_02.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    `Music` tiếp tục dẫn đầu về lượt Like và Comment trung bình trên mỗi video. Ngược lại, `News & Politics` có tỷ lệ Like/Dislike thấp nhất, cho thấy tính chất gây tranh cãi, trong khi `Autos & Vehicles` là thể loại “lành” nhất (tỷ lệ L/D cao nhất).
    """)
    
    st.divider()
    st.subheader("5. Mức độ “cô đặc” kênh")
    st.image("images/category_analysis/04_01.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    Một phát hiện thú vị là thể loại `Sports` có chỉ số video/kênh cao nhất (~45). Điều này ngụ ý rằng một số ít các kênh thể thao lớn (như ESPN, NBA) tạo ra phần lớn các video trending.
    """)
    
    st.divider()
    st.subheader("6. Video hàng đầu")
    st.image("images/category_analysis/05_01.png",use_container_width=True)
    st.image("images/category_analysis/05_02.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    Video “Discord Loot Boxes” (`Entertainment`) thống trị tuyệt đối với 1.4 tỷ lượt xem. Phần còn lại của Top 10 bị chiếm lĩnh bởi K-Pop (BTS, BLACKPINK).
    """)

# ---------------------------------------------------------
# 🕒 PHÂN TÍCH 2: THỜI GIAN
# ---------------------------------------------------------
elif main_topic == "Phân tích Thời gian":
    st.header("🕒 Phân tích Theo Thời gian (Time)")
    st.write("Khám phá xu hướng xuất bản video trending theo Tháng, Ngày, và Giờ trong ngày.")
    
    st.subheader("1. Xu hướng đăng bài theo Ngày")
    st.image("images/time_analysis/02.png", use_container_width=True)
    st.image("images/time_analysis/03.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    Thứ Sáu (Fri) là ngày "bùng nổ" nhất với hơn 44,500 video được đăng (để đón đầu cuối tuần). Tuy nhiên, biểu đồ "Video Trending" lại cho thấy YouTube phân bổ số lượng video thịnh hành rất đều cho mọi ngày trong tuần.
    """)

    st.divider()
    st.subheader("2. Tốc độ lọt Top Trending")
    st.image("images/time_analysis/01.png", use_container_width=True)
    st.image("images/time_analysis/04.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    Phân tích cho thấy tốc độ là yếu tố then chốt. Hầu hết các video (hơn 25,000) lọt vào trending chỉ 1 ngày sau khi đăng. Gần như không thể lọt top trending lần đầu nếu video đã quá 4-5 ngày tuổi.
    """)
    st.markdown("""
    **Phân tích sâu:**
    Các phân tích bổ sung đưa ra một insight quan trọng. Mặc dù 17:00 là giờ đăng phổ biến nhất, các video đăng lúc 09:00 sáng mới là nhóm có lượt xem, like và comment trung bình cao nhất. Điều này cho thấy việc đăng video sớm hơn (ít cạnh tranh hơn) giúp video có cả ngày để tích lũy tương tác.
    """)
    st.image("images/time_analysis/05_02.png", use_container_width=True)

    st.divider()
    st.subheader("3. Heatmap Giờ-Ngày")
    st.image("images/time_analysis/05.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    Biểu đồ nhiệt xác định rõ "giờ vàng" để đăng video là 17:00 (5 giờ chiều) ngày Thứ Sáu.
    """)

# ---------------------------------------------------------
# 💬 PHÂN TÍCH 3: TƯƠNG TÁC
# ---------------------------------------------------------
elif main_topic == "Phân tích Tương tác":
    st.header("💬 Phân tích Tương tác (Interaction)")
    st.write("Khám phá mối tương quan giữa View, Like, Dislike và Comment.")
    
    st.subheader("1. Top 20 Videos")
    st.image("images/interaction_analysis/01.png", use_container_width=True)
    st.image("images/interaction_analysis/02.png", use_container_width=True)
    st.image("images/interaction_analysis/03.png", use_container_width=True)
    st.image("images/interaction_analysis/04.png", use_container_width=True)

    st.markdown("""
    **Nhận xét:**  
    Các bảng xếp hạng Top 20 cho thấy sự khác biệt rõ rệt:
    - **Top Views (Lượt xem):** Bị thống trị bởi MV "Life Goes On" (BTS) và "Discord".
    - **Top Engagement (Tổng tương tác):** Bị thống trị bởi "Shakira: BZRP Session".
    - **Top Likes (Lượt thích):** Bị thống trị bởi video "so long nerds" (tưởng niệm Technoblade).
    - **Top Comments (Bình luận):** Gần như bị độc chiếm bởi K-Pop (JISOO, BTS), cho thấy sức mạnh của fandom trong việc tạo thảo luận.
    """)

    st.divider()
    st.subheader("2. Top 20 Tỷ lệ Tương tác")
    st.image("images/interaction_analysis/05.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    Khi đo lường "chất lượng" (tỷ lệ % tương tác trên mỗi lượt xem), K-Pop (BTS, Stray Kids) thống trị tuyệt đối. Các video này có tỷ lệ tương tác lên đến 30-40%, cho thấy một cộng đồng fan cực kỳ trung thành.
    """)

    st.divider()
    st.subheader("3. Tương tác theo Thể loại")
    st.image("images/interaction_analysis/06.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    Thể loại: `Comedy` (Hài) và `Music` (Âm nhạc) có tỷ lệ tương tác (Engagement Rate) và tỷ lệ Like trung bình cao nhất.
    """)
    
    st.divider()
    st.subheader("4. Phân tích Tương quan")
    st.image("images/interaction_analysis/07.png",use_container_width=True)
    st.image("images/interaction_analysis/07_01.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    Ma trận nhiệt và biểu đồ tán xạ cung cấp insight quan trọng nhất:
    - **Tương quan dương mạnh (0.685):** Giữa `Likes` (Thích) và `Comments` (Bình luận).
    - **Tương quan dương (0.628):** Giữa `Views` (Xem) và `Likes` (Thích).
    - **Không tương quan/Âm yếu (-0.023):** Giữa `Views` (Xem) và `Engagement Rate` (Tỷ lệ tương tác). Điều này khẳng định rằng: **nhiều lượt xem không có nghĩa là tỷ lệ tương tác cao**. Các video "siêu viral" (vài trăm triệu view) thường có tỷ lệ tương tác thấp, trong khi các video có fandom mạnh (vài chục triệu view) lại có tỷ lệ tương tác cao vượt trội.
    """)
    
# ---------------------------------------------------------
# ⚡ PHÂN TÍCH 4: REALTIME
# ---------------------------------------------------------
elif main_topic == "Giám sát Thời gian thực":
    st.header("Giám sát Thời gian thực (Real-time)")
    st.write("Nhấn nút bên dưới để chạy giám sát trong 10 phút (cập nhật mỗi 2 phút).")
    st.divider()

    if st.button("BẮT ĐẦU GIÁM SÁT"):
        
        with st.spinner("Đang chạy giám sát... (Việc này sẽ mất 10 phút)..."):
            try:
                # 1. GỌI HÀM LẤY DỮ LIỆU
                # (Hàm này sẽ chạy trong 10 phút và trả về 1 DataFrame)
                history_df = realtime_logic.continuous_monitoring(
                    duration_minutes=10, 
                    interval_seconds=60
                )
                
                # 2. GỌI HÀM VẼ (Dùng data vừa lấy)
                fig_summary = realtime_logic.plot_results(history_df) 
                
                # 3. HIỂN THỊ KẾT QUẢ
                
                if fig_summary is not None:
                    st.subheader("Bảng điều khiển Tóm tắt (Sau 10 phút)")
                    # Dùng st.pyplot để hiển thị 'fig'
                    st.pyplot(fig_summary, use_container_width=True) 
                    
                    st.subheader("Dữ liệu Lịch sử Chi tiết")
                    # Dùng st.dataframe để hiển thị bảng
                    st.dataframe(history_df, use_container_width=True) 
                    
                    st.success("Giám sát hoàn tất!")
                else:
                    st.warning("⚠️ Không có dữ liệu lịch sử để hiển thị.")
                    
            except Exception as e:
                st.error(f"Đã xảy ra lỗi khi chạy: {e}")
    
    else:
        st.info("Nhấn nút để bắt đầu.")
