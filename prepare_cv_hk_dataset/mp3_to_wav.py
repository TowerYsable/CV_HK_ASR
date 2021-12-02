'''
Author: your name
Date: 2021-11-02 12:22:06
LastEditTime: 2021-11-02 12:22:07
LastEditors: your name
Description: In User Settings Edit
FilePath: /wavs/mp3_to_wav.py
'''
from pydub import AudioSegment
import os

def MP32WAV(mp3_path, wav_path):
    """
    这是MP3文件转化成WAV文件的函数
    :param mp3_path: MP3文件的地址
    :param wav_path: WAV文件的地址
    """
    MP3_File = AudioSegment.from_mp3(file=mp3_path)
    MP3_File = MP3_File.set_frame_rate(16000)
    MP3_File.export(wav_path, format="wav")
# MP32WAV('F:/mp3/3.mp3','F:/mp3/3.wav')


import os
import re

path = '/media/tower/其它/asr_dataset/cv-corpus-7.0-2021-07-21-zh-HK/cv-corpus-7.0-2021-07-21/zh-HK/raw_ki/dev'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        #print(str(file))
        re_filename = re.findall('.\w+', str(file))
        split_file = re_filename[0]+re_filename[1]+".wav"
        #split_file_2 = re_filename[1]
        #print(split_file)
        MP32WAV("dev/"+str(file),"dev_wavs/"+split_file)
        
        #os.rename(os.path.join(path,file),os.path.join(path,split_file))

from pathlib import Path
mixed_test_dir = Path(path)
mixed_train_files = sorted(list(mixed_test_dir.rglob('*.wav')))
print(mixed_train_files)

