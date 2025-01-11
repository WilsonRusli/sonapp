import streamlit as st

st.title("Son Application")
st.write("Masukkan nama brand")

brand = st.text_input("Masukkan text: ")
cam = st.camera_input("Say cheese")
t = st.color_picker("Hello")

if brand:
    st.write("Teks anda adalah")
    st.write(brand)