import streamlit as st
from PIL import Image
import pytesseract
from bs4 import BeautifulSoup
import os
import json
from dotenv import load_dotenv
from urllib.request import Request, urlopen
import requests
import urllib.error
import time


# Set path ke binary Tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

tab1, tab2 = st.tabs(["Picture to Text", "Lyric Finder"])

with tab1:
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
            "DOUGHNUT GULA": "04933"
            
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


with tab2:
    # Load environment variables from .env file
    load_dotenv(dotenv_path="geniusAPI.env")

    # Get the Genius API key from environment variables
    GENIUS_API_KEY = os.getenv("client_access_token")
    
    st.title("Lyric Finder")
    st.write("Cari lirik lagu favorit Anda di sini.")

    def fetch_lyric():
        search_term = st.text_input("Masukkan nama lagu:").replace(" ", "_")
        if not search_term:
            return

        if not GENIUS_API_KEY:
            st.error("API key is missing. Please set the GENIUS_API_KEY.")
            return
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Access-Control-Allow-Origin": "*"
        }
        genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={GENIUS_API_KEY}"
        req = Request(genius_search_url, headers=headers)

        try:
            response = urllib.request.urlopen(req)
            json_data = response.read().decode('utf-8')

            json_data = json.loads(json_data)
            if 'response' in json_data and 'hits' in json_data['response']:
                hits = json_data['response']['hits']
                if hits:
                    song_url = hits[0]['result']['url']

                    # Fetch the lyrics page
                    lyric_page = Request(song_url, headers=headers)
                    st.write(f"URL lagu: {song_url}")
                    time.sleep(1)
                    lyrics_response = urllib.request.urlopen(lyric_page)

                    html = lyrics_response.read().decode('utf-8')
                    soup = BeautifulSoup(html, 'html.parser')

                    lyrics_div = soup.find('div', class_='lyrics') or soup.find('div', class_='Lyrics-sc-37019ee2-1 jRTEBZ')
                    if lyrics_div:
                        lyrics = lyrics_div.get_text(separator='\n').strip()
                        st.text_area("Lirik lagu:", lyrics, height=400)
                    else:
                        st.error("Lyrics not found on the page.")
                        
        except urllib.error.HTTPError as e:
            st.error(f"HTTPError: {e.code} - {e.reason}")
        except urllib.error.URLError as e:
            st.error(f"URLError: {e.reason}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")
            
    fetch_lyric()

# with tab2:
#     st.title("Lyric Finder")
#     st.write("Cari lirik lagu favorit Anda di sini.")

#     def fetch_lyric():
#         search_term = st.text_input("Masukkan nama lagu:")
#         if not search_term:
#             return

#         if not GENIUS_API_KEY:
#             st.error("API key is missing. Please set the GENIUS_API_KEY.")
#             return

#         genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={GENIUS_API_KEY}"
#         headers = {
#             "Content-Type": "application/json",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#         }

#         try:
#             response = requests.get(genius_search_url, headers=headers)
#             response.raise_for_status()  # Raise an error for bad status codes
#             json_data = response.json()

#             if 'response' in json_data and 'hits' in json_data['response']:
#                 hits = json_data['response']['hits']
#                 if hits:
#                     song_url = hits[0]['result']['url']

#                     # Fetch the lyrics page
#                     session = requests.Session()
#                     session.headers.update(headers)

#                     lyrics_response = session.get(song_url, headers=headers)
#                     lyrics_response.raise_for_status()
#                     soup = BeautifulSoup(lyrics_response.text, 'html.parser')

#                     # Find the lyrics
#                     lyrics_div = soup.find('div', class_='lyrics') or soup.find('div', class_='Lyrics-sc-37019ee2-1 jRTEBZ')
#                     if lyrics_div:
#                         lyrics = lyrics_div.get_text(separator='\n')
#                         st.text_area("Lirik lagu:", lyrics, height=400)
#                     else:
#                         st.error("Lyrics not found on the page.")
#                 else:
#                     st.error("No hits found for the search term.")
#             else:
#                 st.error("Invalid response from Genius API.")
#         except requests.exceptions.HTTPError as http_err:
#             st.error(f"HTTP error occurred: {http_err}")
#             st.write(http_err.response.text)  # Log the response text for more details
#         except Exception as err:
#             st.error(f"An error occurred: {err}")
#             st.write(str(err))  # Log the error message for more details

#     fetch_lyric()

