from pytube import YouTube
# misc
import os
import shutil
import math
import datetime
# plots
import matplotlib.pyplot as plt
# image operation
import cv2

vid = YouTube('https://www.youtube.com/watch?v=xVxNyL8xQ7U')

for stream in vid.streams.filter(file_extension='mp4'):
    print(stream)
    
vid.streams.get_by_itag(299).download()