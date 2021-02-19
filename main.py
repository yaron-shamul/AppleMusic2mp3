from pytube import YouTube
from lxml import html
import subprocess
import requests
import os


class Song():
	def __init__(self, name, artist, album):
		self.name = name
		self.artist = artist
		self.album = album

	def __repr__(self):
		return f'{self.name} | {self.artist} | {self.album}'


'''
will take data from 'data' file
'''
def data_parser():
	songs = []

	with open('data') as f:
		for song_info in f.read().split('\n')[:5]:
			song_info = song_info.split('\t')
			songs.append(Song(song_info[0], song_info[3], song_info[4]))

	return songs


'''
will search for the song in youtube and return
the link for the first song
'''
def yt_url_by_name(song):

	URL_TEMPLATE = f'https://www.youtube.com/results?search_query={song}'.replace('|', '')
	
	r = requests.get(URL_TEMPLATE)
	results = r.text.find('watch?v=')

	watch_link = r.text[results : results + 19]
	print('# Song url found...')
	return f'https://www.youtube.com/{watch_link}'
	

def download_by_url(song, url):
	print(f'# Start Downloading {song.name}...')
	yt = YouTube(url) 
	stream = yt.streams.filter(only_audio=True).first()

	path = 'C:\\Users\\Yaron Shamul\\Desktop\\apple music\\songs\\' + str({song.name})[2:-2]
	stream.download(path)
	print();print();print()
	



if __name__ == '__main__':
	for song in data_parser():
		download_by_url(song, yt_url_by_name(song))
		
	#yt_url_by_name()
