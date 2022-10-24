import numpy as np
import wave
import pyaudio
import scipy.io.wavfile as wav
import pickle
import audiolazy.lazy_lpc as method
from hmmlearn.hmm import GaussianHMM as hmm
#import data_processing as dp


def initialize(inputWav):
    rate, signal = wav.read(inputWav)  # returns a wave_read object , rate: sampling frequency
    return signal, rate

def lowPassFilter(signal, coeff=0.95):
    return np.append(signal[0],
                     signal[1:] - coeff * signal[:-1])  # y[n] = x[n] - a*x[n-1] , a = 0.97 , a>0 for low-pass filters

def preEmphasis(wav):
    signal, rate = initialize(wav)
    emphasizedSignal = lowPassFilter(signal)
    return emphasizedSignal, signal, rate


def record(namefile):
    print('========================================record========================================')
    # the file name output you want to record into
    filename = (namefile+".wav")
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 2
    # 44100 samples per second
    sample_rate = 8000
    record_seconds = 2
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(8000 / chunk * record_seconds)):
        data = stream.read(chunk)
        # if you want to hear your voice while recording
        # stream.write(data)
        frames.append(data)
    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()

    print('========================================test========================================')
    for i in range(1):
        i = i + 1

        print('record save as ',filename)

        emphasizedSignal, signal, rate = preEmphasis(filename)
        filt = method.lpc(emphasizedSignal,8)
        lpc_features = filt.numerator[1:]
        lpc_refeatures = np.reshape(lpc_features, (-1, 1))  # reshape reshape to matrix

        max_score = -float("inf")
        max_label = 0

        for j in range(540):
            j = j + 1

            model = pickle.load(open("data/model_english/model_" + str(j) + ".pkl", 'rb'))

            scr = model.score(lpc_refeatures)  # method score menggunakan algorithm="forward"

            if scr > max_score:
                max_score = scr
                max_label = j

        if (max_label >= 1) and (max_label <= 25):
            label_predict = 'fisika'
        elif (max_label >= 26) and (max_label <= 50):
            label_predict = 'matematika'
        elif (max_label >= 51) and (max_label <= 75):
            label_predict = 'bahasa inggris'
        elif (max_label >= 76) and (max_label <= 100):
            label_predict = 'bahasa inggris'
        elif (max_label >= 101) and (max_label <= 125):
            label_predict = 'bahasa inggris'

        #mean, freqz = dp.spectral_statistics(signal, rate)
        #print("mean : ", mean)
        print("predicted data -", str(max_label), " label = ", label_predict)

    return label_predict


