import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np


file = "blues.00000.wav"
# waveform
signal_np, sr = librosa.load(file, sr=22050) # => sr*T-> 22050*30
# librosa.display.waveshow(signal_np, sr=sr)

# plt.xlabel("Time")
# plt.ylabel(f"Amplitude")
# plt.show()

# fft -> spectrum
# fft = np.fft.fft(signal_np)
# magnitude = np.abs(fft)
# frequency = np.linspace(0, sr, len(magnitude))
# left_frequency = frequency[:int(len(frequency)/2)]
# left_magnitude = magnitude[:int(len(frequency)/2)]

# plt.plot(left_frequency, left_magnitude)
# plt.xlabel("left_frequency")
# plt.ylabel("left_magnitude")
# plt.show()

# stft -> spectrogram

n_fft = 2048
hope_length = 512

stft = librosa.core.stft(signal_np, hop_length=hope_length, n_fft = n_fft)
spectrogram = np.abs(stft)

log_spectrogram = librosa.amplitude_to_db(spectrogram)

# librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hope_length)
# plt.xlabel("time")
# plt.ylabel("frequency")
# plt.colorbar()
# plt.show()

# MFFCC
mfcc = librosa.feature.mfcc(y = signal_np,sr=sr, n_mfcc=13, n_fft=n_fft, hop_length=hope_length)
# mffc = librosa.feature.mfcc(signal_np, n_fft=n_fft, hop_length=hope_length, n_mfcc=13)
# print(len(mfcc))
librosa.display.specshow(mfcc, sr=sr, hop_length=hope_length)
plt.xlabel("time")
plt.ylabel("mffc")
plt.colorbar()
plt.show()