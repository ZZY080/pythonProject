import librosa
import numpy as np
from pydub import AudioSegment

# 加载音频文件
input_file = "./ss.m4a"
output_file = "output_audio.m4a"
y, sr = librosa.load(input_file)

# 增强低音
y_shifted = np.roll(y, 3000)  # 调整这个值以控制低音的增强程度

# 输出增强低音后的音频
librosa.output.write_wav(output_file, y_shifted, sr)
print("超重低音处理完成，输出文件名为: ", output_file)
