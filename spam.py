import uuid
import sounddevice
from scipy.io.wavfile import write
import os
import wave
for file_name in os.listdir(FOLD):
    with wave.open(file_name, "rb") as wave_file:
        frame_rate = wave_file.getframerate()



#fs=44100
#second=3
#print("recording.....")
#record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
#sounddevice.wait()
#print("done.....")
#write(str(uuid.uuid1())+".wav",fs,record_voice)


#import wave
#import pyaudio

# the file name output you want to record into
#print("----mulai---")
#filename = (str(uuid.uuid1())+".wav")
# set the chunk size of 1024 samples
#chunk = 1024
# sample format
#FORMAT = pyaudio.paInt16
# mono, change to 2 if you want stereo
#channels = 2
# 44100 samples per second
#sample_rate = 8000
#record_seconds = 3
# initialize PyAudio object
#p = pyaudio.PyAudio()
# open stream object as input & output
#stream = p.open(format=FORMAT, channels=channels,rate=sample_rate,input=True,output=True,frames_per_buffer=chunk)
#frames = []
#print("Recording...")
#for i in range(int(8000 / chunk * record_seconds)):
#    data = stream.read(chunk)
    # if you want to hear your voice while recording
    # stream.write(data)
#    frames.append(data)
#print("Finished recording.")
# stop and close stream
#stream.stop_stream()
#stream.close()
# terminate pyaudio object
#p.terminate()
# save audio file
# open the file in 'write bytes' mode
#wf = wave.open(filename, "wb")
# set the channels
#wf.setnchannels(channels)
# set the sample format
#wf.setsampwidth(p.get_sample_size(FORMAT))
# set the sample rate
#wf.setframerate(sample_rate)
# write the frames as bytes
#wf.writeframes(b"".join(frames))
# close the file
#wf.close()

#print('========================================testing========================================')