# load dependencies
import pandas as pd
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import csv





# load file
sample, data  = wav.read("258135_24_M_20_1.wav", mmap=False)

# rescale samples into time
time = np.linspace(0, len(data)-1, len(data)) / sample

#plot
plt.plot(data)
plt.xlabel('wave')
plt.show()

# load labels
labels = list(csv.reader(open("258135_24_M_20_1.txt", 'r'), delimiter='\t'))
labels

# divide wave into words
commands = dict{}

list_elo = []
for label in labels:
    list_elo.append(label[0])

print(list_elo)