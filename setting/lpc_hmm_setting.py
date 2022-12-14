import numpy as np
import wave
import pyaudio
import scipy.io.wavfile as wav
import pickle
import audiolazy.lazy_lpc as method
from hmmlearn.hmm import GaussianHMM as hmm


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


def lpc_hmm_train():
    print('========================================train========================================')
    for i in range(17):
        i = i + 1
        audio = 'data_training/_ (' + str(i) + ').wav'

        emphasizedSignal, signal, rate= preEmphasis(audio)
        filt = method.lpc(emphasizedSignal, 8)
        lpc_features = filt.numerator[1:]

        lpc_refeatures = np.reshape(lpc_features, (-1, 1))  # reshape to matrix
        #print('LPC Reshape Feature ke -', i, ' = ', lpc_refeatures)
        model = hmm(n_iter=10).fit(lpc_refeatures)  #hmm default

        with open("model_training/model_"+ str(i) + ".pkl", "wb") as file: pickle.dump(model, file)
        print('Create model and save model as model_',str(i))
    return lpc_features

def lpc_hmm_uji_all():
    match = 0
    scr_value = []
    print('========================================test all========================================')
    for i in range(20):
        i = i + 1

        audio = 'data_uji/fisika/bumi/_ (' + str(i) + ').wav'

        print(audio)

        if (i >= 1) and (i <= 20):
            label_actual = 'bumi'


        print('actual label = ',label_actual)

        emphasizedSignal, signal, rate= preEmphasis(audio)
        filt = method.lpc(emphasizedSignal, 8)
        lpc_features = filt.numerator[1:]
        lpc_refeatures = np.reshape(lpc_features, (-1, 1))  # reshape to matrix

        max_score = -float("inf")
        max_label = 0

        for j in range(96):
            j = j + 1

            model = pickle.load(open("model/fisika/model_ (" + str(j) + ").pkl", 'rb'))

            scr = model.score(lpc_refeatures) #method score menggunakan algorithm="forward"
            scr_value.append(scr)
            if scr > max_score:
                max_score = scr
                max_label = j

        if (max_label >= 1) and (max_label <= 20):
            label_predict = 'bumi'
        elif (max_label >= 21) and (max_label <= 40):
            label_predict = 'gerak'
        elif (max_label >= 41) and (max_label <= 59):
            label_predict = 'planet'
        elif (max_label >= 60) and (max_label <= 80):
            label_predict = 'gerak melingkar'
        elif (max_label >= 81) and (max_label <= 96):
            label_predict = 'tata surya'

        if label_actual==label_predict:
            status = 'detected'
            if label_predict == 'bumi':
                match= match+1
        else:
            status = 'undetected'

        print("predicted data -", str(max_label), " label = ", label_predict," status = ",status)
        #mean, freqz = dp.spectral_statistics(emphasizedSignal, rate)
        #print("LPCF : ", lpc_refeatures)
        #print("Mean : ", mean)
        #print("Score : ", max_score)
        #print("all score : ",scr_value)

        result = 'match = '+str(match)
    return result

def lpc_hmm_uji_one(fname):
    scr_value = []
    print('========================================test========================================')
    for i in range(1):
        i = i + 1

        print(fname)

        emphasizedSignal, signal, rate= preEmphasis(fname)
        print(signal)
        print(rate)
        filt = method.lpc(emphasizedSignal,8)
        lpc_features = filt.numerator[1:]
        lpc_refeatures = np.reshape(lpc_features, (-1, 1))  # reshape reshape to matrix

        max_score = -float("inf")
        max_label = 0

        for j in range(96):
            j = j + 1

            model = pickle.load(open("model/fisika/model_ ("+ str(j) + ").pkl", 'rb'))

            scr = model.score(lpc_refeatures) #method score menggunakan algorithm="forward"
            scr_value.append(scr)
            if scr > max_score:
                max_score = scr
                max_label = j

        if (max_label >= 1) and (max_label <= 20):
            label_predict = 'bumi'
        elif (max_label >= 21) and (max_label <= 40):
            label_predict = 'gerak'
        elif (max_label >= 41) and (max_label <= 59):
            label_predict = 'planet'
        elif (max_label >= 60) and (max_label <= 80):
            label_predict = 'gerak melingkar'
        elif (max_label >= 81) and (max_label <= 96):
            label_predict = 'tata surya'



        print("predicted data -", str(max_label), " label = ", label_predict, " status = ")
        result = "predicted data -" + str(max_label) + " label = " + label_predict + " status = "
        print("Max Score : ", max_score)
        # print("All Score : ",scr_value)

    return result,label_predict

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

    if filename.find('whatsapp') > -1:
        label_actual = 'whatsapp'
    elif filename.find('linkedin') > -1:
        label_actual = 'linkedin'
    elif filename.find('tokopedia') > -1:
        label_actual = 'tokopedia'
    elif filename.find('tokopedia') > -1:
        label_actual = 'tokopedia'
    elif filename.find('tokopedia') > -1:
        label_actual = 'tokopedia'
    else:
        label_actual = 'undetected'

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

            model = pickle.load(open("code/umum/model_hmm_16/model_" + str(j) + ".pkl", 'rb'))

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

        if signal <= 780:
            result = ' suara kurang jelas suaranya sehingga tidak dapat di deteksi'
            label_predict = ""
        elif label_actual == "undetected":
            result = ' data suara tidak ada pada database'
            label_predict = ""
        else:
            print("predicted data -", str(max_label), " label = ", label_predict)
            result = "predicted data -" + str(max_label) + " label = " + label_predict

    return result, label_predict


