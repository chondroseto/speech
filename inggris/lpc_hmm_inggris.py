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
    filename = (namefile+".wav")
    fs = 44100
    second = 3
    print("recording.....")
    record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
    sounddevice.wait()
    print("done.....")
    wav.write(filename, fs, record_voice)

    print('========================================testing========================================')

    print('record save as ',filename)

    emphasizedSignal, signal, rate = preEmphasis(filename)
    filt = method.lpc(emphasizedSignal,8)
    lpc_features = filt.numerator[1:]
    lpc_refeatures = np.reshape(lpc_features, (-1, 1))  # reshape reshape to matrix

    max_score = -float("inf")
    max_label = 0

    for j in range(112):
        j = j + 1

        model = pickle.load(open("inggris/model_training/model_ (" + str(j) + ").pkl", 'rb'))

        scr = model.score(lpc_refeatures)  # method score menggunakan algorithm="forward"

        if scr > max_score:
            max_score = scr
            max_label = j

    if (max_label >= 1) and (max_label <= 34):
        label_predict = 'Comparison'
    elif (max_label >= 35) and (max_label <= 53):
        label_predict = 'Diagnostic Test'
    elif (max_label >= 54) and (max_label <= 69):
        label_predict = 'Present Continuous Tense'
    elif (max_label >= 70) and (max_label <= 86):
        label_predict = 'Verb'
    elif (max_label >= 87) and (max_label <= 112):
        label_predict = 'Final Test'


        #mean, freqz = dp.spectral_statistics(signal, rate)
        #print("mean : ", mean)

    #if signal <= 400:
        #result = 'suara kurang jelas suaranya sehingga tidak dapat di deteksi'
        #label_predict = ""
    #else:
        #print("predicted data -", str(max_label), " label = ", label_predict)
        #result = "predicted data -" + str(max_label) + " label = " + label_predict

    #print(result)
    print("predicted data -", str(max_label), " label = ", label_predict)
    more_lines = ['\n---test---',str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' -  predicted data - '+str(max_label)+' label = '+label_predict,'---end_test---']
    with open('history_log.txt', 'a') as f:
        f.write('\n'.join(more_lines))
    #result='detected'
    return label_predict


