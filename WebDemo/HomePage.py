import streamlit as st
#import lib.common as tools

st.set_page_config(
    page_title="Đồ án cuối kỳ",
    page_icon="☕",
)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://png.pngtree.com/thumb_back/fw800/background/20200714/pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg");
    background-size: 100% 100%;
}
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right:2rem;
}
[data-testid="stSidebar"] > div:first-child {
    background-image: url("https://wallpaperaccess.com/full/1510605.jpg");
    background-position: center;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)


# logo_path = "./VCT.png"
# st.sidebar.image(logo_path, width=200)

st.write("# Đồ án cuối kỳ")
st.write("# 20133093 - Nguyễn Minh Tiến")
st.write("# Mã lớp : DIPR430685_22_2_10")

st.markdown(
    """
    ## Sản phẩm
    Project cuối kỳ cho môn học xử lý ảnh số DIPR430685.
    Thuộc Trường Đại Học Sư Phạm Kỹ Thuật TP.HCM.
    ### 3 chức năng chính trong bài
    - 🧭Nhận diện khuôn mặt
    - 👩Phát hiện khuôn mặt
    - 🌅Xử lý ảnh số (Bao gồm 4 chương: 3, 4, 5, 9)
    ## Thông tin sinh viên thực hiện
    - 🧑Họ tên: Nguyễn Minh Tiến
    - 💳MSSV: 20133093
    
    """
)


