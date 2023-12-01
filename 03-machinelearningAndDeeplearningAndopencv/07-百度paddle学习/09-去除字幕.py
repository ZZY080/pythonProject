import subprocess

# 输入视频文件名和输出文件名
input_file = 'E:\onedrive\桌面\inputvideo.mp4'
output_file = 'output_video.mp4'
#ffmpeg -i input.mkv -vf "ass=subs.ass" -c:v libx264 -crf 20 -c:a ac3 output.mkv
# 使用FFmpeg去除字幕
subprocess.call(['ffmpeg', '-i', input_file, '-vf', '-c:v', 'copy', '-c:a', 'copy', output_file])
