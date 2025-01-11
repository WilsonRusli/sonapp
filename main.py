import streamlit as st
from PIL import Image
import pytesseract

# Set konfigurasi Tesseract jika diperlukan
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_text_from_image(image):
    """Fungsi untuk mendeteksi teks dari gambar menggunakan pytesseract."""
    text = pytesseract.image_to_string(image)
    return text

# Judul aplikasi
st.title("Text Detection from Image")
st.write("Unggah gambar dan dapatkan teks yang terdeteksi dari gambar tersebut.")

# Upload gambar
guploaded_file = st.file_uploader("Unggah gambar Anda di sini", type=["jpg", "png", "jpeg"])

if guploaded_file is not None:
    # Buka gambar menggunakan PIL
    image = Image.open(guploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_column_width=True)

    # Tampilkan teks yang terdeteksi
    with st.spinner("Mendeteksi teks dari gambar..."):
        detected_text = detect_text_from_image(image)

    st.subheader("Teks yang Terdeteksi:")
    st.text_area("", detected_text, height=200)

    if st.button("Simpan teks ke file"):
        with open("detected_text.txt", "w", encoding="utf-8") as f:
            f.write(detected_text)
        st.success("Teks telah disimpan ke 'detected_text.txt'")
