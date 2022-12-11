import string
import os
from moviepy.editor import *

""" 
mp4dir: string == the relative Path to the mp4-file
outputdir: string == the relatie path to the output dir
mp3dir: string == the name for the output-file. Should end with '.mp3'
"""
def convert(mp4dir: string, mp3name: string, outputdir: string) -> None:
    video = VideoFileClip(os.path.join(mp4dir))
    video.audio.write_audiofile(os.path.join(outputdir,mp3name))
    video.close()

convert("example_video.mp4","output_name.mp3")