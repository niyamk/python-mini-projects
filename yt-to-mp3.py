# importing packages 
from pytube import YouTube 
import os 

yt = YouTube(str(input("enter url : ")))

audio = yt.streams.filter(only_audio=True).first()

print("destination ? ( blank for E:\songs )")
des = input(':') or 'E:\songs'
print('processing...')
op_file = audio.download(output_path=des)

try:
    base, ext = os.path.splitext(op_file) 
    new_file = base + '.mp3'
    os.rename(op_file, new_file) 
except :
    print('something went wrong.')
else:
    print('download complete...')