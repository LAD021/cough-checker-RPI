#-*-coding:utf-8-*-

import pyaudio
import wave
import config
import os
from pydub import AudioSegment

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = config.CHANNELS
RATE = 44100
RECORD_SECONDS = config.RECORD_SECONDS

def getSound():
    try:
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print("* 开始记录")

        frames = []
        forward = RECORD_SECONDS
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            now = RECORD_SECONDS - i / (RATE / CHUNK)
            if now < forward:
                print("* 还有{}秒".format(now))
                forward = now
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(config.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        val = os.system("ffmpeg -y -i ./output/sound.wav ./output/soundp.mp3")
#        print(val)
        sound = AudioSegment.from_mp3("./output/soundp.mp3")
        louder_sound = sound + 10 
        louder_sound.export("./output/sound.mp3", format='mp3')
        
        print("* 记录完成")        

        return 0
    
    except Exception as e:
        print(e)
        p.terminate()
        return -1

