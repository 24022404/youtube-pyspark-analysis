import streamlit as st
from datetime import datetime

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
st.caption("Thực hiện bởi: Nhóm Big Data - Hùng & Các bạn | Cập nhật: " + datetime.now().strftime("%d/%m/%Y"))
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

    st.subheader("1. Thể loại phổ biến nhất (Theo tần suất)")
    st.image("images/category_analysis/01.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    - 🎵 *Music* là thể loại chiếm tỷ lệ cao nhất.  
    - Các thể loại như *Entertainment* và *Gaming* cũng có số lượng video đáng kể.
    """)

    st.divider()
    st.subheader("2. Thể loại có tổng lượt xem cao nhất")
    st.image("images/category_analysis/02.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    - 🎵 *Music* vượt trội về tổng lượt xem.  
    - Khi loại bỏ *Music*, *Entertainment* và *News & Politics* nổi bật hơn.
    """)

    st.divider()
    st.subheader("3. Thể loại có nhiều Channel nhất")
    st.image("images/category_analysis/03.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    - Các thể loại phổ biến như *Music* và *Entertainment* có nhiều kênh hơn.  
    - *Education* và *Science & Technology* tuy ít kênh hơn nhưng thường mang nội dung chuyên sâu.
    """)
    
    st.divider()
    st.subheader("4. Mức độ Tương tác theo Thể loại")
    st.image("images/category_analysis/04.png",use_container_width=True)
    st.image("images/category_analysis/04_01.png",use_container_width=True)
    st.image("images/category_analysis/04_02.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    hhhhhhhhh
    """)
    
    st.divider()
    st.subheader("5. Video Hàng đầu theo Từng Thể loại")
    st.image("images/category_analysis/05_01.png",use_container_width=True)
    st.image("images/category_analysis/05_02.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    hhhhhhhhh
    """)

# ---------------------------------------------------------
# 🕒 PHÂN TÍCH 2: THỜI GIAN
# ---------------------------------------------------------
elif main_topic == "Phân tích Thời gian":
    st.header("🕒 Phân tích Theo Thời gian (Time)")
    st.write("Khám phá xu hướng xuất bản video trending theo Tháng, Ngày, và Giờ trong ngày.")
    
    st.subheader("1. ")
    st.image("images/time_analysis/01.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    hhhhh
    """)

    st.divider()
    st.subheader("2. ")
    st.image("images/time_analysis/02.png", use_container_width=True)
    st.markdown("""
    hhhhh
    """)

    st.divider()
    st.subheader("3. ")
    st.image("images/time_analysis/03.png",use_container_width=True)
    st.markdown("""
    hhhhhhh
    """)
    
    st.divider()
    st.subheader("4. ")
    st.image("images/time_analysis/04.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    hhhhhhhhh
    """)
    
    st.divider()
    st.subheader("5. ")
    st.image("images/time_analysis/05.png",use_container_width=True)
    st.image("images/time_analysis/05_01.png",use_container_width=True)
    st.image("images/time_analysis/05_02.png",use_container_width=True)
    st.image("images/time_analysis/05_03.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    hhhhhhhhh
    """)

# ---------------------------------------------------------
# 💬 PHÂN TÍCH 3: TƯƠNG TÁC
# ---------------------------------------------------------
elif main_topic == "Phân tích Tương tác":
    st.header("💬 Phân tích Tương tác (Interaction)")
    st.write("Khám phá mối tương quan giữa View, Like, Dislike và Comment.")
    
    st.subheader("1. ")
    st.image("images/interaction_analysis/01.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    hhhhh
    """)

    st.divider()
    st.subheader("2. ")
    st.image("images/interaction_analysis/02.png", use_container_width=True)
    st.markdown("""
    hhhhh
    """)

    st.divider()
    st.subheader("3. ")
    st.image("images/interaction_analysis/03.png",use_container_width=True)
    st.markdown("""
    hhhhhhh
    """)
    
    st.divider()
    st.subheader("4. ")
    st.image("images/interaction_analysis/04.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    hhhhhhhhh
    """)
    
    st.divider()
    st.subheader("5. ")
    st.image("images/interaction_analysis/05.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    hhhhhhhhh
    """)
    
    st.divider()
    st.subheader("6. ")
    st.image("images/interaction_analysis/06.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    hhhhhhhhh
    """)
    
    st.divider()
    st.subheader("7. ")
    st.image("images/interaction_analysis/07.png",use_container_width=True)
    st.image("images/interaction_analysis/07_01.png",use_container_width=True)
    st.image("images/interaction_analysis/07_02.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**  
    hhhhhhhhh
    """)

# ---------------------------------------------------------
# ⚡ PHÂN TÍCH 4: REALTIME
# ---------------------------------------------------------
elif main_topic == "Giám sát Thời gian thực":
    st.header("Giám sát Thời gian thực (Real-time)")
    st.write("Nhấn nút bên dưới để chạy giám sát trong 10 phút (cập nhật mỗi 5 phút).")
    st.divider()

    if st.button("BẮT ĐẦU GIÁM SÁT"):
        
        with st.spinner("Đang chạy giám sát... (Việc này sẽ mất 10 phút)..."):
            try:
                # 1. GỌI HÀM LẤY DỮ LIỆU
                # (Hàm này sẽ chạy trong 10 phút và trả về 1 DataFrame)
                history_df = realtime_logic.continuous_monitoring(
                    duration_minutes=10, 
                    interval_seconds=300
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
