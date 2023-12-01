import requests
import os
# import pyttsx3
import tkinter
import webbrowser


# import  requests
# url=input('请输入视频的url:')
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
# response = requests.get(url, headers=headers, stream=True)
# video_size = response.headers['content-length']
# print(f'视频大小为{int(int(int(video_size) / 1024) / 1024)}M')
# data = response.content
# with open(r'E:/网易云音乐下载/solo.mp4', 'wb')as file:
#     file.write(data)
# os.system('ffmpeg -i "E:/网易云音乐下载/暨南大学1.mp4" -i "E:/网易云音乐下载/把回忆拼好给你.mp3" -c copy "E:/网易云音乐下载/暨南大学3.mp4" ')
# os.remove('fly.mp4')
#os.system(r'ffmpeg -i "12.mp4" -vn -y -acodec copy 龙卷风.m4a -loglevel quiet')
# saying = pyttsx3.init()
# saying.say('音频抽取成功')
# saying.runAndWait()

# os.system(r'ffmpeg -i "E:\onedrive\桌面\1.m4a" -i "E:\onedrive\桌面\1.mp4" -c copy "黑客1.mp4" ')
# print('a')

from  moviepy.editor import *

clipVideo1 = VideoFileClip(r"E:\onedrive\桌面\kenny.mp4")
clipVideo2 = VideoFileClip(r"E:\onedrive\桌面\kenny4.mp4")
video = concatenate_videoclips([clipVideo1,clipVideo2],'compose')
video.write_videofile(r'E:\onedrive\桌面\kenny5.mp4')






