import streamlit as st

st.title("Son Application")
st.write("Masukkan nama brand")

brand = st.text_input("Masukkan nama anda")
cam = st.camera_input("Say cheese")
t = st.color_picker("Hello")

# print all data
with open("database.csv", "r") as f:
    data = f.readlines()

st.write(data)

if brand:
    st.write("Teks anda adalah")
    # save to database "database.csv"
    
    with open("database.csv", "a") as f:
        f.write(brand + "\n")
    

    

    st.write("Created by felix")
    st.write(brand)