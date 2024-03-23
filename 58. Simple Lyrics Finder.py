import requests
from bs4 import BeautifulSoup

def find_lyrics(artist, song_title):
    url = f"https://www.azlyrics.com/lyrics/{artist.lower().replace(' ', '')}/{song_title.lower().replace(' ', '')}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    lyrics_div = soup.find('div', class_='col-xs-12 col-lg-8 text-center')
    if lyrics_div:
        lyrics = lyrics_div.text.strip()
        print(lyrics)
    else:
        print("Lyrics not found.")

def main():
    artist = input("Enter artist name: ")
    song_title = input("Enter song title: ")
    find_lyrics(artist, song_title)

if __name__ == "__main__":
    main()
