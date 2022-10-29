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


def lpc_hmm_train():
    print('========================================train========================================')
    for i in range(540):
        i = i + 1
        audio = 'code/umum/data_train/_ (' + str(i) + ').wav'

        emphasizedSignal, signal, rate= preEmphasis(audio)
        filt = method.lpc(emphasizedSignal, 8)
        lpc_features = filt.numerator[1:]

        lpc_refeatures = np.reshape(lpc_features, (-1, 1))  # reshape to matrix
        #print('LPC Reshape Feature ke -', i, ' = ', lpc_refeatures)
        model = hmm(n_iter=10).fit(lpc_refeatures)  #hmm default

        with open("code/umum/model_hmm/model_"+ str(i) + ".pkl", "wb") as file: pickle.dump(model, file)
        print('Create model and save model as model_',str(i))
    return lpc_features

def lpc_hmm_uji_all():
    fisika_match = 0
    matematika_match = 0
    inggris_match = 0
    data_uji_per_class = 20
    scr_value = []
    print('========================================test all========================================')
    for i in range(120):
        i = i + 1

        audio = 'code/umum/data_uji/_ (' + str(i) + ').wav'

        print(audio)

        if (i >= 1) and (i <= 20):
            label_actual = 'fisika'
        elif (i >= 21) and (i <= 40):
            label_actual = 'matematika'
        elif (i >= 41) and (i <= 60):
            label_actual = 'bahasa inggris'

        print('actual label = ',label_actual)

        emphasizedSignal, signal, rate= preEmphasis(audio)
        filt = method.lpc(emphasizedSignal, 8)
        lpc_features = filt.numerator[1:]
        lpc_refeatures = np.reshape(lpc_features, (-1, 1))  # reshape to matrix

        max_score = -float("inf")
        max_label = 0

        for j in range(540):
            j = j + 1

            model = pickle.load(open("code/umum/model_hmm/model_" + str(j) + ".pkl", 'rb'))

            scr = model.score(lpc_refeatures) #method score menggunakan algorithm="forward"
            scr_value.append(scr)
            if scr > max_score:
                max_score = scr
                max_label = j

        if (max_label >= 1) and (max_label <= 90):
            label_predict = 'fisika'
        elif (max_label >= 91) and (max_label <= 180):
            label_predict = 'matematika'
        elif (max_label >= 181) and (max_label <= 270):
            label_predict = 'bahasa inggris'

        if label_actual==label_predict:
            status = 'detected'
            if label_predict == 'fisika':
                fisika_match= fisika_match+1
            elif label_predict == 'matematika':
                matematika_match = matematika_match + 1
            elif label_predict == 'bahasa inggris':
                inggris_match = inggris_match + 1
        else:
            status = 'undetected'

        #print("predicted data -", str(max_label), " label = ", label_predict," status = ",status)
        #mean, freqz = dp.spectral_statistics(emphasizedSignal, rate)
        #print("LPCF : ", lpc_refeatures)
        #print("Mean : ", mean)
        #print("Score : ", max_score)
        #print("all score : ",scr_value)

        result = 'Detection Persentase rate= '+str((fisika_match+matematika_match+inggris_match)/(data_uji_per_class*3)*100)+'% \n Fisika = '+str((fisika_match/data_uji_per_class)*100)+'%\n Matematika = '+str((matematika_match/data_uji_per_class)*100)+' %\n Bahasa Inggris = '+str((inggris_match/data_uji_per_class)*100)+'%'
    return result

def lpc_hmm_uji_one(fname):
    scr_value = []
    print('========================================test========================================')
    for i in range(1):
        i = i + 1

        print(fname)

        if fname.find('fisika')>-1:
            label_actual = 'fisika'
        elif fname.find('matematika') > -1:
            label_actual = 'matematika'
        elif fname.find('inggris') > -1:
            label_actual = 'bahasa inggris'
        else:
            label_actual = 'undetected'

        print('actual label = ',label_actual)

        emphasizedSignal, signal, rate= preEmphasis(fname)
        filt = method.lpc(emphasizedSignal,8)
        lpc_features = filt.numerator[1:]
        lpc_refeatures = np.reshape(lpc_features, (-1, 1))  # reshape reshape to matrix

        max_score = -float("inf")
        max_label = 0

        for j in range(540):
            j = j + 1

            model = pickle.load(open("code/umum/model_hmm/model_"+ str(j) + ".pkl", 'rb'))

            scr = model.score(lpc_refeatures) #method score menggunakan algorithm="forward"
            scr_value.append(scr)
            if scr > max_score:
                max_score = scr
                max_label = j

        if (max_label>=1)and(max_label<=90):
            label_predict = 'fisika'
        elif (max_label>=91)and(max_label<=180):
            label_predict = 'matematika'
        elif (max_label>=181)and(max_label<=270):
            label_predict = 'bahasa inggris'

        if label_actual==label_predict:
            status = 'detected'
        else:
            status = 'undetected'


        if signal <= 780:
            result = 'file suara kurang jelas suaranya sehingga tidak dapat di deteksi'
            label_predict = ""
        elif label_actual == 'undetected':
            result = 'data suara tidak ada pada database'
            label_predict = ''
        else:
            print("predicted data -", str(max_label), " label = ", label_predict, " status = ", status)
            result = "predicted data -" + str(max_label) + " label = " + label_predict + " status = " + status
            #print("mean : ", mean)
            print("Max Score : ", max_score)
            # print("All Score : ",scr_value)

    return result,label_actual,label_predict,status

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

        if (max_label >= 1) and (max_label <= 90):
            label_predict = 'fisika'
        elif (max_label >= 91) and (max_label <= 180):
            label_predict = 'matematika'
        elif (max_label >= 181) and (max_label <= 270):
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


