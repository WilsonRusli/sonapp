from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

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

print("Lyric Finder")
print("Cari lirik lagu favorit Anda di sini.")
GENIUS_API_KEY = "heEvE7HHjU1NH4Sa9ma0it6mhpye593tSO5dsanbTzs_ZG8KPhcEQupaBZRBcJ-G"
search_term = input("Masukkan nama lagu: ")
if search_term:
    genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={GENIUS_API_KEY}"
    print(genius_search_url)
    try:
        req = Request(genius_search_url, headers={"User-Agent": "Mozilla/5.0"})
        response = urlopen(req)

        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        lyrics_div = soup.find('div', class_='Lyrics-sc-37019ee2-1 jRTEBZ')
        if lyrics_div:
            lyrics = lyrics_div.get_text(separator='\n').strip()
            print("Lirik yang Ditemukan:")
            print(lyrics)
        else:
            print("Lyrics not found")
    except Exception as e:
        print(f"Error fetching lyrics: {e}")