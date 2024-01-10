from pytube import YouTube
import sys
from sys import argv
length = len(sys.argv)
list = argv [1]
yt = YouTube(list)

print("Title: ", yt.title)

print("Number of views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download("C:/Users/shiva/Downloads/")