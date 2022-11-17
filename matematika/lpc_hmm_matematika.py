import numpy as np
import sounddevice
import scipy.io.wavfile as wav
import pickle
import audiolazy.lazy_lpc as method
import datetime


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
    filename = (namefile + ".wav")
    fs = 44100
    second = 3
    print("recording.....")
    record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
    sounddevice.wait()
    print("done.....")
    wav.write(filename, fs, record_voice)


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

        for j in range(96):
            j = j + 1

            model = pickle.load(open("matematika/model_training/model_ (" + str(j) + ").pkl", 'rb'))

            scr = model.score(lpc_refeatures)  # method score menggunakan algorithm="forward"

            if scr > max_score:
                max_score = scr
                max_label = j

        if (max_label >= 1) and (max_label <= 39):
            label_predict = 'bangun ruang'
        elif (max_label >= 40) and (max_label <= 78):
            label_predict = 'pecahan'
        elif (max_label >= 79) and (max_label <= 96):
            label_predict = 'perbandingan'
        elif (max_label >= 97) and (max_label <= 135):
            label_predict = 'luas bangun ruang'
        elif (max_label >= 136) and (max_label <= 175):
            label_predict = 'operasi pecahan'

        print("predicted data -", str(max_label), " label = ", label_predict)
        more_lines = ['\n---test---',
                      str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' -  predicted data - ' + str(
                          max_label) + ' label = ' + label_predict, '---end_test---']
        with open('history_log.txt', 'a') as f:
            f.write('\n'.join(more_lines))

    return label_predict


