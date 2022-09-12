from operator import indexOf
from pytube import YouTube
import string
import os
from moviepy.editor import *
import sys

def download_video(url: string, name: string)-> bool:
    #downloadet ein youtube video von einer URL und convertiert es zu einer mp3
    try:
        yt = YouTube(url)
        yd = yt.streams.get_highest_resolution()
        m=name+".mp4"
        yd.download("data/mp4", m)
        n=name+".mp3"
        convert(m,n)
        delete_mp4(m)
        error = False
    except:
        error = True
    return error
def convert(m: string, n: string):
    #convertiert eine mp4 zur mp3
    video = VideoFileClip(os.path.join("data\mp4",m))
    video.audio.write_audiofile(os.path.join("data\mp3",n))
    video.close()
def delete_mp4(m: string):
    #löscht eine mp4
    os.remove(os.path.join("data","mp4",m))
def get_input()-> string:
    args = sys.argv[1::]
    input_args = args[0]
    return input_args
def get_pos_trennung(input_args: string)-> int:
    pos_trennung = indexOf(input_args, ";")
    return pos_trennung
def get_url(input_args: string,pos_trennung: string)-> string:
    url = input_args[0:pos_trennung-1]
    return url
def get_name(input_args: string,pos_trennung: string)-> string:
    name = input_args[pos_trennung+1::]
    return name

input_str = get_input()
pos_trennung = get_pos_trennung(input_str)
yturl = get_url(input_str, pos_trennung)
name = get_name(input_str, pos_trennung)
error = download_video(yturl, name)
if error == False:
    print("Downloadet")
elif error == True:
    print("Error")
    print("Es ist ein Fehler aufgetreten")