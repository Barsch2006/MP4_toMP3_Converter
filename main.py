import string
import os
from moviepy.editor import *
from pytube import YouTube

mp4folder = "" # dir to put the .mp4 files
mp3folder = "" # output dir to put the .mp3 files
urlfile = "" # .txt file of urls

def download(yt) -> string:
    yt.download(mp4folder, yt.title) # download video
    return mp4folder + yt.title # return path of downloaded video

def convert(mp4path, mp3name) -> None:
    video = VideoFileClip(os.path.join(mp4path))
    video.audio.write_audiofile(os.path.join(mp3folder, mp3name))
    video.close()
    if os.path.exists(mp4path): # delete mp4
        os.remove(mp4path)

def getUrls(filepath):
    # read filepath of urls an return the urls as list
    f = open(filepath, 'r')
    lines = f.readlines()
    urls = []
    for line in lines:
        urls.append(line[0:-1])
    return urls

def main():
 for url in getUrls(urlfile):
        try:
            yt = YouTube(url)
            yt = yt.streams.get_highest_resolution() # get the highest resulution for best audio
            mp4dir = download(yt) #download file
            mp3name = yt.title + ".mp3"
            convert(mp4dir, mp3name)
            num = num + 1 # to get number of files

        except: # on Error print download number and continue
            print("Error nicht möglich #" + str(num))
            num = num + 1
            continue
        print(num + " files downloaded")

main()