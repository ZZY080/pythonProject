import moviepy.editor as mp

# 采样率16k 保证和paddlespeech一致
def extract_audio(videos_file_path):
     my_clip = mp.VideoFileClip(videos_file_path,audio_fps=16000)
     if (videos_file_path.split(".")[-1] == 'MP4' or videos_file_path.split(".")[-1] == 'mp4'):
          p = videos_file_path.split('.MP4')[0]
          my_clip.audio.write_audiofile(p + '_video.wav')
          new_path = p + '_video.wav'
     return new_path

import auditok
import os


def qiefen(path, ty='video', mmin_dur=1, mmax_dur=100000, mmax_silence=1, menergy_threshold=55):

    file = path

    audio_regions = auditok.split(
        file,
        min_dur=mmin_dur,  # minimum duration of a valid audio event in seconds
        max_dur=mmax_dur,  # maximum duration of an event
        # maximum duration of tolerated continuous silence within an event
        max_silence=mmax_silence,
        energy_threshold=menergy_threshold  # threshold of detection
    )

    for i, r in enumerate(audio_regions):
        # Regions returned by `split` have 'start' and 'end' metadata fields
        print(
            "Region {i}: {r.meta.start:.3f}s -- {r.meta.end:.3f}s".format(i=i, r=r))

        epath = ''
        file_pre = str(epath.join(file.split('.')[0].split('/')[-1]))

        mk = '/change'
        if (os.path.exists(mk) == False):
            os.mkdir(mk)
        if(os.path.exists(mk+'/'+ty) == False):
            os.mkdir(mk+'/'+ty)
        if(os.path.exists(mk+'/'+ty+'/'+file_pre) == False):
            os.mkdir(mk+'/'+ty+'/'+file_pre)

        num = i
        # 为了取前三位数字排序
        s = '000000'+str(num)

        file_save = mk+'/'+ty+'/'+file_pre + '/' + \
            s[-3:]+'-'+'{meta.start:.3f}-{meta.end:.3f}'+'.wav'

        filename = r.save(file_save)
        print("region saved as: {}".format(filename))

    return mk+'/'+ty+'/'+file_pre

import paddle
from paddlespeech.cli import ASRExecutor, TextExecutor

import warnings
warnings.filterwarnings('ignore')

asr_executor = ASRExecutor()
text_executor = TextExecutor()

def audio2txt(path):

    # 返回path下所有文件构成的一个list列表
    filelist = os.listdir(path)
    # 保证读取按照文件的顺序
    filelist.sort(key=lambda x: int(x[:3]))
    # 遍历输出每一个文件的名字和类型
    words = []
    for file in filelist:
        print(path+'/'+file)
        text = asr_executor(
            audio_file=path+'/'+file,
            device=paddle.get_device())
        if text:
            result = text_executor(
                text=text,
                task='punc',
                model='ernie_linear_p3_wudao',
                device=paddle.get_device())
        else:
            result = text
        words.append(result)
    return words

import csv

def txt2csv(txt):
    with open(path+'.csv', 'w', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        for row in txt_all:
            f_csv.writerow([row])

# 拿到新生成的音频的路径
path = extract_audio('99.mp4')

# 划分音频
path = qiefen(path=path, ty='video',
              mmin_dur=0.5, mmax_dur=100000, mmax_silence=0.5, menergy_threshold=55)

# 音频转文本  需要GPU
txt_all = audio2txt(path)

# 存入csv
txt2csv(txt_all)