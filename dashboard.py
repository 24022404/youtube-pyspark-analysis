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
    - 📈 *Entertainment* (53,934 video) và *Gaming* (53,242 video) là hai thể loại xuất hiện trên top trending **thường xuyên nhất**, với số lượng gần như tương đương nhau.
    - 🎵 *Music* (43,398 video) theo sát ở vị trí thứ 3. Ba thể loại hàng đầu này chiếm phần lớn các video lọt vào top thịnh hành trong tập dữ liệu lịch sử.
    - 📉 Các thể loại như *Pets & Animals* (1,222) và đặc biệt là *Nonprofits & Activism* (120) có tần suất xuất hiện rất thấp.
    """)

    st.divider()
    st.subheader("2. Thể loại có tổng lượt xem cao nhất")
    st.image("images/category_analysis/02.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    - 🎵 Mặc dù *Music* chỉ đứng thứ 3 về tần suất xuất hiện, đây lại là thể loại **dẫn đầu tuyệt đối** về **tổng lượt xem** (36.1 tỷ), cho thấy mỗi video âm nhạc khi lọt vào trending thường có lượt xem rất lớn.
    - 🎭 *Entertainment* (33.0 tỷ) theo sát ở vị trí thứ hai. Hai thể loại này bỏ xa phần còn lại.
    - 🎮 *Gaming* (16.5 tỷ) dù xuất hiện thường xuyên nhưng tổng lượt xem chỉ bằng một nửa so với Music hay Entertainment.
    """)

    st.divider()
    st.subheader("3. Thể loại có nhiều Channel nhất")
    st.image("images/category_analysis/03.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    - 🏆 Ba thể loại hàng đầu về tần suất video (`Entertainment`, `Music`, `Gaming`) cũng là ba thể loại có số lượng kênh (channel) duy nhất tham gia vào top trending nhiều nhất, đều trên 1,700 kênh.
    - ⚔️ Điều này cho thấy đây là các "sân chơi" có tính cạnh tranh rất cao, với hàng ngàn kênh khác nhau đã từng lọt vào top thịnh hành, chứ không bị thống trị bởi một vài kênh duy nhất.
    - 🧑‍🤝‍🧑 *People & Blogs* cũng cho thấy sự đa dạng cao với 1,113 kênh tham gia.
    """)
    
    st.divider()
    st.subheader("4. Mức độ Tương tác theo Thể loại")
    st.image("images/category_analysis/04.png",use_container_width=True)
    st.image("images/category_analysis/04_01.png",use_container_width=True)
    st.image("images/category_analysis/04_02.png",use_container_width=True)
    st.markdown("""
    **Nhận xét (Từ 3 biểu đồ):**
    - ❤️ **Vua tương tác:** *Music* dẫn đầu tuyệt đối về lượt **Like** và **Comment** trung bình trên mỗi video. Tuy nhiên, nó cũng dẫn đầu về lượt **Dislike** trung bình, cho thấy mức độ tương tác cao ở mọi khía cạnh.
    - ⚖️ **Tỷ lệ Like/Dislike (Mức độ yêu thích):** Biểu đồ "Tỷ lệ L/D" cho thấy thể loại "được yêu thích nhất" (ít gây tranh cãi nhất) là *Autos & Vehicles*. Ngược lại, *News & Politics* có tỷ lệ L/D thấp nhất, cho thấy đây là thể loại phân cực và gây tranh cãi nhiều nhất.
    - 📈 **Mức độ "cô đặc" kênh:** *Sports* có chỉ số video/kênh cao nhất (~45). Điều này có nghĩa là một số ít các kênh lớn (như ESPN, NBA) tạo ra phần lớn các video trending cho thể loại này. Ngược lại, *Music* và *People & Blogs* có chỉ số này thấp, cho thấy sự đa dạng hơn về kênh (nhiều kênh nhỏ cùng lọt top).
    """)
    
    st.divider()
    st.subheader("5. Video Hàng đầu theo Từng Thể loại")
    st.image("images/category_analysis/05_01.png",use_container_width=True)
    st.image("images/category_analysis/05_02.png",use_container_width=True)
    st.markdown("""
    **Nhận xét (Từ 2 biểu đồ):**
    - 🥇 **Video Vô địch Tuyệt đối:** Video "Discord Loot Boxes are here" (thuộc *Entertainment*) là video có lượt xem cao nhất trong toàn bộ tập dữ liệu với hơn 1.4 tỷ lượt xem, vượt xa tất cả các video khác.
    - 🇰🇷 **Sức mạnh K-Pop:** Phần còn lại của Top 10 chung cuộc bị thống trị gần như hoàn toàn bởi *Music*, cụ thể là các MV của **BLACKPINK** và **BTS**.
    - 🎮 Biểu đồ "Lượt xem *Vô địch* từng Thể loại" cho thấy rõ sự chênh lệch: video *Entertainment* top 1 (Discord) có lượt xem gấp ~5 lần video `Music` top 1 (BLACKPINK - *Pink Venom*, ~278 triệu view) và gấp ~8 lần video *Gaming* top 1 (GTA VI Trailer, ~166 triệu view).
    """)

# ---------------------------------------------------------
# 🕒 PHÂN TÍCH 2: THỜI GIAN
# ---------------------------------------------------------
elif main_topic == "Phân tích Thời gian":
    st.header("🕒 Phân tích Theo Thời gian (Time)")
    st.write("Khám phá xu hướng xuất bản video trending theo Giờ, Ngày trong tuần, và Tốc độ lọt vào top thịnh hành.")
    
    st.subheader("1. Phân bố Đăng video (theo Giờ trong Ngày)")
    st.image("images/time_analysis/01.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    * **Giờ cao điểm:** 17:00 (5 giờ chiều) là giờ có nhiều video được đăng và lọt top trending nhất (với 15,446 video).
    * **Xu hướng:** Lượng video bắt đầu tăng mạnh từ 14:00 (2 giờ chiều) và đạt đỉnh lúc 17:00, sau đó giảm dần vào buổi tối.
    * **Giờ thấp điểm:** 4:00 - 6:00 sáng là thời điểm có ít video được đăng nhất.
    * **Insight:** Đa số các nhà sáng tạo nhắm đến khung giờ chiều tối để đăng video, có thể để đón lượng khán giả tan làm hoặc tan học.
    """)

    st.divider()
    st.subheader("2. Phân bố Đăng video (theo Ngày trong Tuần)")
    st.image("images/time_analysis/02.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    * 🚀 **Thứ Sáu (Fri)** là ngày "bùng nổ" nhất, khi có đến 44,575 video được đăng và sau đó lọt vào trending. Các nhà sáng tạo dường như nhắm đến ngày này để đón đầu lượng người xem cuối tuần.
    * 🗓️ Các ngày trong tuần (Thứ Hai - Thứ Sáu) có lượng video đăng cao và khá ổn định (từ 36,000 đến 44,000).
    * 📉 **Thứ Bảy (Sat)** là ngày có ít video được đăng nhất (34,892), cho thấy các kênh thường nghỉ ngơi hoặc đã đăng video vào Thứ Sáu.
    """)

    st.divider()
    st.subheader("3. Phân bố Video Thịnh Hành (theo Ngày trong Tuần)")
    st.image("images/time_analysis/03.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    * ⚖️ Một phát hiện thú vị: Mặc dù số lượng video *đăng* vào Thứ Sáu cao vượt trội (biểu đồ trên), số lượng video *hiển thị* trên tab trending lại được phân bổ **cực kỳ đồng đều** qua tất cả các ngày trong tuần (khoảng 38,000 - 39,000 video mỗi ngày).
    * 🔄 Điều này cho thấy thuật toán của YouTube luôn cố gắng duy trì một số lượng video thịnh hành ổn định mỗi ngày, bất kể video đó được đăng vào ngày nào.
    """)
    
    st.divider()
    st.subheader("4. Phân bố Thời gian chờ lọt Top Trending")
    st.image("images/time_analysis/04.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    * ⚡ **Tốc độ là Vua:** Hầu hết các video lọt vào trending đều làm điều đó rất nhanh.
    * 📈 Đỉnh cao tuyệt đối là **1 ngày** sau khi đăng (hơn 25,000 video). Ngày thứ 2 cũng rất cao (khoảng 17,500 video).
    * ⏳ Rất hiếm video có thể lọt vào top trending lần đầu tiên nếu đã quá 4-5 ngày kể từ khi xuất bản. Điều này nhấn mạnh tầm quan trọng của việc tạo ra "cú hích" tương tác trong 48 giờ đầu tiên.
    """)
    
    st.divider()
    st.subheader("5. Phân tích sâu: Heatmap Giờ-Ngày, Tương tác & Tuổi thọ")
    st.image("images/time_analysis/05.png",use_container_width=True)
    st.image("images/time_analysis/05_01.png",use_container_width=True)
    st.image("images/time_analysis/05_02.png",use_container_width=True)
    st.image("images/time_analysis/05_03.png",use_container_width=True)
    st.markdown("""
    **Nhận xét (Từ 4 biểu đồ):**
    * 🔥 **"Giờ Vàng" để đăng bài (Heatmap):** Biểu đồ nhiệt cho thấy "điểm nóng" nhất để đăng video là **17:00 (5 giờ chiều) ngày Thứ Sáu (Fri)**, với hơn 6,900 video. Nhìn chung, khung giờ 14:00 - 18:00 các ngày trong tuần là thời điểm phổ biến nhất để đăng video.
    * 🏆 **"Giờ Vàng" để có tương tác (Biểu đồ đường):** Tuy nhiên, biểu đồ đường "Tương tác trung bình" lại chỉ ra rằng các video được đăng lúc **9:00 sáng** có xu hướng đạt được **lượt xem, like và comment trung bình cao nhất**.
    * 💡 **Insight quan trọng:** Đăng video vào 17:00 (lúc mọi người cùng đăng) có thể chịu cạnh tranh rất cao. Đăng vào 9:00 sáng (giờ ít phổ biến hơn) dường như giúp video có cả ngày để tích lũy tương tác và đạt đỉnh vào buổi tối.
    * ⏳ **"Tuổi thọ" trên Trending (Biểu đồ cột):** Hầu hết các video trụ lại trên top trending trung bình từ 5.5 đến 6 ngày. Video `Sports` (thường là tin tức/highlight) có tuổi thọ ngắn nhất (~5.2 ngày), trong khi `Music` (MV) có xu hướng trụ lại lâu hơn một chút (~6.1 ngày).
    * ⏱️ **Tốc độ Trending (Biểu đồ cột):** Tốc độ lọt top trending của các thể loại nhìn chung là **khá tương đồng nhau**, với hầu hết các video mất trung bình từ 1.4 đến 1.6 ngày sau khi đăng.
    """)

# ---------------------------------------------------------
# 💬 PHÂN TÍCH 3: TƯƠNG TÁC
# ---------------------------------------------------------
elif main_topic == "Phân tích Tương tác":
    st.header("💬 Phân tích Tương tác (Interaction)")
    st.write("Khám phá mối tương quan giữa Lượt xem, Lượt thích, Bình luận và Tỷ lệ Tương tác của các video thịnh hành.")
    
    st.subheader("1. Top 20 Video theo Lượt xem (Views)")
    st.image("images/interaction_analysis/01.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    * 🥇 **Thống trị tuyệt đối:** MV "Life Goes On" của **BTS** đứng đầu với 1.4 TỶ lượt xem, một con số khổng lồ, bỏ xa video thứ hai.
    * 🎶 **Âm nhạc & Creator:** Top 20 bị thống trị bởi hai nhóm chính: Các MV K-Pop (BTS, LISA, BLACKPINK) và các video/shorts từ các creator lớn (MrBeast - "1v1", "Face Your Biggest Fear", video Discord).
    * 💰 Các video có kinh phí sản xuất cao hoặc video shorts có tính lan truyền mạnh chiếm ưu thế rõ rệt về tổng lượt xem.
    """)

    st.divider()
    st.subheader("2. Top 20 Video theo Tổng Tương tác (Likes + Comments + Dislikes)")
    st.image("images/interaction_analysis/02.png", use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    * 💃 **Sức mạnh Latin & K-Pop:** Bản hit của **Shakira** (BZRP Music Session) tạo ra lượng tương tác tổng cộng lớn nhất (77.8 triệu), cho thấy sức ảnh hưởng toàn cầu.
    * 🖤💖 **K-Pop thống trị:** Các thành viên solo của BLACKPINK (ROSÉ, JISOO) và BTS (J-Hope, Jung Kook) chiếm phần lớn các vị trí còn lại, chứng tỏ lượng fan trung thành và tích cực tương tác.
    * 💡 **View không phải là tất cả:** Video "Discord" (top view ở mục 1) thậm chí không xuất hiện trong top 20 này. Điều này cho thấy video nhiều view nhất không đồng nghĩa với video nhiều tương tác (like/comment) nhất.
    """)

    st.divider()
    st.subheader("3. Top 20 Video theo Lượt Thích (Likes)")
    st.image("images/interaction_analysis/03.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    * ❤️ **Sức mạnh Cảm xúc:** Video "so long nerds" (video tưởng niệm Technoblade) có lượt like cao nhất (16.0 triệu), cho thấy nội dung mang tính cảm xúc, gắn kết cộng đồng có thể tạo ra làn sóng ủng hộ mạnh mẽ.
    * 🤝 **Creator & Âm nhạc:** Top 20 là sự kết hợp giữa các video nhân văn của creator (MrBeast - "1,000 Blind People...") và các MV âm nhạc lớn (Shakira, K-Pop).
    * 🎵 Lượt "Like" là một chỉ số mạnh mẽ về sự yêu thích, và cả nội dung cảm xúc lẫn âm nhạc đều làm rất tốt điều này.
    """)
    
    st.divider()
    st.subheader("4. Top 20 Video theo Lượt Bình luận (Comments)")
    st.image("images/interaction_analysis/04.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    * 🗣️ **Fandom K-Pop thống trị:** Biểu đồ này gần như bị độc chiếm bởi K-Pop (JISOO, BTS, BLACKPINK, LISA, ROSÉ, J-Hope, EXO, TWICE...).
    * 📈 **Bình luận = Chỉ số Vàng của Fandom:** Lượt bình luận là chỉ số rõ ràng nhất cho thấy sự tồn tại của một cộng đồng fan (fandom) năng động, có tổ chức, và tích cực "cày view/comment" cho thần tượng.
    * 💬 Video teaser (của BTS) cũng có lượt comment cực cao, cho thấy sự mong đợi và thảo luận lớn ngay cả trước khi sản phẩm chính ra mắt.
    """)
    
    st.divider()
    st.subheader("5. Top 20 Video theo Tỷ lệ Tương tác (Engagement Rate)")
    st.image("images/interaction_analysis/05.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    * ✨ **Tỷ lệ Vàng:** "Tỷ lệ tương tác" (phần trăm người xem có tương tác) là chỉ số đo lường "chất lượng" của lượt xem, thay vì "số lượng".
    * ❤️‍🔥 **K-Pop Vô đối:** Một lần nữa, K-Pop (BTS, Stray Kids, ATEEZ, TXT) thống trị tuyệt đối. Các video này có thể không có view cao bằng video của MrBeast, nhưng tỷ lệ fan tương tác trên mỗi lượt xem là cực kỳ cao.
    * 📱 **Shorts & Challenge:** Video "Permission to Dance" (Shorts Challenge) của BTS có tỷ lệ tương tác rất cao (33.7%), cho thấy định dạng video ngắn và các thử thách (challenge) khuyến khích tương tác mạnh mẽ.
    """)
    
    st.divider()
    st.subheader("6. Chỉ số Tương tác Trung bình (theo Thể loại)")
    st.image("images/interaction_analysis/06.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    * 😂 **Hài hước & Âm nhạc:** `Comedy` (Hài kịch) và `Music` (Âm nhạc) là hai thể loại (ngoại trừ "Unknown") có tỷ lệ tương tác (Engagement Rate) và tỷ lệ like (Like Rate) trung bình cao nhất. Khán giả xem hài và âm nhạc có xu hướng tương tác tích cực.
    * 🗣️ `Music` cũng dẫn đầu về tỷ lệ comment (Comment Rate) trung bình.
    * 📰 **Gây tranh cãi:** `News & Politics` (Tin tức) có tỷ lệ like và comment trung bình thấp nhất, nhưng lại có tỷ lệ dislike trung bình cao nhất. Điều này một lần nữa khẳng định tính chất phân cực của thể loại này.
    """)
    
    st.divider()
    st.subheader("7. Phân tích Tương quan (Heatmap & Biểu đồ Tán xạ)")
    st.image("images/interaction_analysis/07_01.png",use_container_width=True)
    st.image("images/interaction_analysis/07.png",use_container_width=True)
    st.markdown("""
    **Nhận xét:**
    * 👍 **View và Like (Tương quan 0.628):** Có mối tương quan dương mạnh mẽ. Như biểu đồ tán xạ "Views vs Likes" cho thấy, video càng nhiều view thì càng có nhiều like.
    * 💬 **Like và Comment (Tương quan 0.685):** Đây là mối tương quan mạnh nhất giữa các chỉ số tương tác. Một video được nhiều người thích cũng sẽ kích thích nhiều người bình luận.
    * 📉 **View và Tỷ lệ Tương tác (Tương quan -0.023):** *Đây là insight quan trọng nhất.* Biểu đồ "Views vs Engagement Rate" cho thấy các video "siêu viral" (hàng trăm triệu view) thường có **tỷ lệ tương tác thấp**. Tỷ lệ tương tác cao nhất (20-40%) thường được tìm thấy ở các video có lượng view vừa phải, cho thấy các cộng đồng fan nhỏ nhưng trung thành sẽ tương tác mạnh mẽ hơn.
    * 📊 **Heatmap:** Ma trận nhiệt xác nhận rằng `like_rate` (Tỷ lệ like) gần như là yếu tố quyết định chính cho `engagement_rate` (Tỷ lệ tương tác tổng) với tương quan 0.992.
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
                    duration_minutes=2, 
                    interval_seconds=30
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
