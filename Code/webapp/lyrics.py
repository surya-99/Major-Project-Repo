from bs4 import BeautifulSoup
from lyrics_extractor import Song_Lyrics

GCS_API_KEY='AIzaSyASpbvc4JUJ8IrGpD8s0fce-Z5-fR-fVMg'
GCS_ENGINE_ID='017219377714881096991:vkzb1r4mghe'
SONG_NAME= input('Enter Song Name =>')

extract_lyrics = Song_Lyrics(GCS_API_KEY, GCS_ENGINE_ID)
song_title, song_lyrics = extract_lyrics.get_lyrics(SONG_NAME)

print(song_lyrics)