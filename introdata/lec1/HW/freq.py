#coding=UTF-8

import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

count = {
    u'у':0, 
    u'е':0, 
    u'ё':0, 
    u'ы':0, 
    u'а':0, 
    u'о':0, 
    u'э':0, 
    u'я':0, 
    u'и':0, 
    u'ю':0
}

total = 0

def print_freq(d, t):
    for k in d.keys():
    	freq = d[k]/1.0/t
        print(k.encode('utf8')+': '+str(freq))

try:
    filename = sys.argv[1]
except:
    filename = 'input.txt'
    
try:
    with open(filename, 'r') as f:
        for line in f:
            for ch in line.decode('utf8').lower():
                if ch.isalnum() : total += 1
                if ch in count.keys(): count[ch] += 1
except:
    print('Error of reading '+filename)
    exit()

print('Частотность русских гласных в тексте:')
print_freq(count, total)

matplotlib.rc('font', family= 'Arial, Liberation Sans')
plt.bar(np.arange(len(count)), count.values())
plt.xticks(np.arange(len(count)), count.keys())
plt.show()
