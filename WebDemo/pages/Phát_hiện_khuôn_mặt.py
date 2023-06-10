import streamlit as st
import time
import numpy as np
import cv2 as cv
import object_detection as od
import FaceDetection.Haarcascade.app as ha
import FaceDetection.Facebook.face_detect as fb
from PIL import Image

st.set_page_config(page_title="Phát hiện khuôn mặt", page_icon="👩")

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
st.markdown("# Phát hiện khuôn mặt")


selected = st.sidebar.radio("Options", ["Facebook", "Haarcascade"])

if selected == "Facebook":
    fb.main_loop()
elif selected== "Haarcascade":
    ha.main_loop()


st.button("Re-run")
