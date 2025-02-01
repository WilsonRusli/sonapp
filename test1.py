from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request("https://genius.com/For-revenge-serana-lyrics", headers={"User-Agent": "Mozilla/5.0"})
response = urlopen(req)

html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

lyrics_div = soup.find('div', class_='Lyrics-sc-37019ee2-1 jRTEBZ')
if lyrics_div:
    lyrics = lyrics_div.get_text(separator='\n').strip()
    print(lyrics)
else:
    print("Lyrics not found")