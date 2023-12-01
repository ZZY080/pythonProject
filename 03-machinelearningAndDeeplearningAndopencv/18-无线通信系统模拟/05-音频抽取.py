import moviepy.editor as mp
my_clip = mp.VideoFileClip("E:\onedrive\桌面\download (92).mp4")#ci此处为视频的绝对路径。
my_clip.audio.write_audiofile(r'E:\onedrive\桌面\river.mp3')#此处为输出的音频名称和格式
