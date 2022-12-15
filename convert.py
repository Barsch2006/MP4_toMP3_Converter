import string
import os
from moviepy.editor import *
from pytube import YouTube


def convert(mp4dir: string, mp3name: string, outputdir: string) -> None:
    video = VideoFileClip(os.path.join(mp4dir))
    video.audio.write_audiofile(os.path.join(outputdir,mp3name))
    video.close()
    if os.path.exists(mp4dir):
        os.remove(mp4dir)


def download(yt):
    yt.download("G:\YTDownloader\output\mp4", yt.title)
    return "G:\YTDownloader\output\mp4/" + yt.title

def getURLs():
    f = open("G:\YTDownloader/try.txt", 'r')
    lines = f.readlines()
    urls = []
    for line in lines:
        urls.append(line[0:-1])
    num = 1
    for url in urls:
        try:
            yt = YouTube(url)
            yt = yt.streams.get_highest_resolution()
            mp4dir = download(yt)
            mp3name = yt.title + ".mp3"
            convert(mp4dir, mp3name, "G:\YTDownloader\output\sec_try")
            num = num + 1
        except:
            print("Error nicht möglich #" + str(num))
            num = num + 1
            continue

def readDir(dir):
    i=0
    for file in os.listdir("G:\YTDownloader\output\sec_try"):
        if file.endswith('.mp3'):
            print(file)
            i+=1
    print('the total number of files: ' +str(i))