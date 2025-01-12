import streamlit as st
from PIL import Image
import pytesseract

# Set konfigurasi Tesseract jika diperlukan
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set path ke binary Tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


def detect_text_from_image(image):
    """Fungsi untuk mendeteksi teks dari gambar menggunakan pytesseract."""
    text = pytesseract.image_to_string(image)
    return text

# Judul aplikasi
st.title("Text Detection from Image")
st.write("Unggah gambar dan dapatkan teks yang terdeteksi dari gambar tersebut.")

# Upload gambar
guploaded_file = st.file_uploader("Unggah gambar Anda di sini", type=["jpg", "png", "jpeg"])
guploaded_file_cam = st.camera_input("Silakan buka kamera anda...")

# Fungsi untuk mengganti teks tertentu dengan angka
def replace_text_with_numbers(text):
    replacements = {
        "BLACK MOON": "18191",
        "CHOCO CHEESE": "29092",
        "CHEESE BUN": "18204",
        "COCONUT BUN": "18205",
        "BURGER BUN @3 PCS": "30432",
        "SANDWITCH 3 IN 1": "26691",
        "TOAST 12": "18220",
        "DOUGHNUT CERES": "18209",
        "SOJU": "04844",
        "MAYO FLOSS": "04890",
        "MELON BUN": "04811",
        "PANDAN KAYA": "26728",
        "DOUGHTNAT GULA": "04933"
        # Tambahkan pasangan teks dan angka lainnya di sini
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

if guploaded_file_cam is not None:
    # Buka gambar menggunakan PIL
    image = Image.open(guploaded_file_cam)
    st.image(image, caption="Gambar yang diunggah", use_container_width=True)

    # Tampilkan teks yang terdeteksi
    with st.spinner("Mendeteksi teks dari gambar..."):
        detected_text = detect_text_from_image(image)

    detected_text = replace_text_with_numbers(detected_text)

    st.subheader("Teks yang Terdeteksi:")
    st.text_area("", detected_text, height=200)

    if st.button("Simpan teks ke file"):
        with open("detected_text.txt", "w", encoding="utf-8") as f:
            f.write(detected_text)
        st.success("Teks telah disimpan ke 'detected_text.txt'")

if guploaded_file is not None:
    # Buka gambar menggunakan PIL
    image = Image.open(guploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_container_width=True)

    # Tampilkan teks yang terdeteksi
    with st.spinner("Mendeteksi teks dari gambar..."):
        detected_text = detect_text_from_image(image)

    detected_text = replace_text_with_numbers(detected_text)

    st.subheader("Teks yang Terdeteksi:")
    st.text_area("", detected_text, height=200)

    if st.button("Simpan teks ke file"):
        with open("detected_text.txt", "w", encoding="utf-8") as f:
            f.write(detected_text)
        st.success("Teks telah disimpan ke 'detected_text.txt'")
