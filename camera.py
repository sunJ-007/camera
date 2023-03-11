import streamlit as sl
from PIL import Image

uploaded_image = sl.file_uploader("Upload Image")
if uploaded_image:
    img = Image.open(uploaded_image)
    grey = img.convert('L')
    sl.image(grey)

with sl.expander('Start Camera'):
    camera_image = sl.camera_input('Camera')

if camera_image:
    img = Image.open(camera_image)
    grey = img.convert('L')
    sl.image(grey)
