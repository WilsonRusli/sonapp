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
    req = Request(genius_search_url, headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req)
    json_data = response.read().decode('utf-8')
    import json
    json_response = json.loads(json_data)
    if 'response' in json_response and 'hits' in json_response['response']:
        hits = json_response['response']['hits']
        if hits:
            song_url = hits[0]['result']['url']
            print(f"Song URL: {song_url}")
        else:
            print("No results found.")
    else:
        print("Unexpected response format")
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

