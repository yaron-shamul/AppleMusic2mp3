from pytube import YouTube
from lxml import html
import subprocess
import requests
import os

BASE_PATH = R'C:\\Users\\Yaron Shamul\\Desktop\\apple music\\songs\\'

class Song():
	def __init__(self, name, artist, album):
		self.name = name
		self.artist = artist
		self.album = album

	def __repr__(self):
		return f'{self.name} {self.artist} {self.album}'

	'''
	will search for the song in youtube and return
	the link for the first song
	'''
	def get_song_yt_url(self):
		print(f'# Working on: {self}')
		URL_TEMPLATE = f'https://www.youtube.com/results?search_query={self}'
		
		r = requests.get(URL_TEMPLATE)
		results = r.text.find('watch?v=')

		watch_link = r.text[results : results + 19]
		print('# Song url found...')
		return f'https://www.youtube.com/{watch_link}'

	
	def download_song_by_url(self, url):
		print(f'# Start Downloading {self.name}...')
		yt = YouTube(url) 
		stream = yt.streams.filter(only_audio=True).first()

		path = 'BASE_PATH' + str({self.name})[2:-2]
		stream.download(path)
		print();print();print()


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
The fllow is basically to firstly take the parsed data and
than to iterate every song
'''
def fllow():
	for song in data_parser():
		try:
			song.download_song_by_url(song.get_song_yt_url())
		except Exception as e: 
			# maybe a good idea is to print this log into a file and make some report
			print(f'# Error while trying to work on: {song.name} \n Error: {e}')
			continue


if __name__ == '__main__':
	fllow()
	


