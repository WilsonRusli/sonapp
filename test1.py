from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.error
import json

# req = Request("https://genius.com/For-revenge-serana-lyrics", headers={"User-Agent": "Mozilla/5.0"})
# response = urlopen(req)

# html = response.read().decode('utf-8')
# soup = BeautifulSoup(html, 'html.parser')

# lyrics_div = soup.find('div', class_='Lyrics-sc-37019ee2-1 jRTEBZ')
# if lyrics_div:
#     lyrics = lyrics_div.get_text(separator='\n').strip()
#     print(lyrics)
# else:
#     print("Lyrics not found")
GENIUS_API_KEY = "heEvE7HHjU1NH4Sa9ma0it6mhpye593tSO5dsanbTzs_ZG8KPhcEQupaBZRBcJ-G"

def fetch_lyric():
    search_term = input("Masukkan nama lagu: ")
    if not search_term:
        return

    if not GENIUS_API_KEY:
        print("API key is missing. Please set the GENIUS_API_KEY.")
        return

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={GENIUS_API_KEY}"
    req = Request(genius_search_url, headers=headers)

    try:
        response = urlopen(req)
        json_data = response.read().decode('utf-8')

        json_data = json.loads(json_data)
        if 'response' in json_data and 'hits' in json_data['response']:
            hits = json_data['response']['hits']
            if hits:
                song_url = hits[0]['result']['url']

                # Fetch the lyrics page
                lyric_page = Request(song_url, headers=headers)
                print(f"URL lagu: {song_url}")
                lyrics_response = urlopen(lyric_page)

                html = lyrics_response.read().decode('utf-8')
                soup = BeautifulSoup(html, 'html.parser')

                lyrics_div = soup.find('div', class_='lyrics') or soup.find('div', class_='Lyrics-sc-37019ee2-1 jRTEBZ')
                if lyrics_div:
                    lyrics = lyrics_div.get_text(separator='\n').strip()
                    print("Lirik lagu:")
                    print(lyrics)
                else:
                    print("Lyrics not found on the page.")
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    # if 'response' in json_data and 'hits' in json_data['response']:
    #     hits = json_data['response']['hits']
    #     if hits:
    #         song_url = hits[0]['result']['url']

    #         # Fetch the lyrics page
    #         req = Request(song_url, headers={"User-Agent": "Mozilla/5.0"})
    #         response = urlopen(req)

    #         html = response.read().decode('utf-8')
    #         soup = BeautifulSoup(html, 'html.parser')
    #         lyrics_div = soup.find('div', class_='Lyrics-sc-37019ee2-1 jRTEBZ')
    #         if lyrics_div:
    #             lyrics = lyrics_div.get_text(separator='\n').strip()
    #             print("Lirik yang Ditemukan:")
    #             print(lyrics)
    #         else:
    #             print("Lyrics not found")
    #     else:
    #         print("No results found.")
    # else:
    #     print("Unexpected response format")
fetch_lyric()
