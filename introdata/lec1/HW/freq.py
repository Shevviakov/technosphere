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

def count_freq(d, t):
    freq = {}
    for k in d.keys():
        freq[k] = d[k]/1.0/t
    return freq

def print_dict(d):
    for k in d.keys():
        print(k.encode('utf8')+': '+str(d[k]))

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
freq = count_freq(count, total)
print_dict(freq)

matplotlib.rc('font', family= 'Arial, Liberation Sans')
plt.bar(np.arange(len(freq)), freq.values(), width=0.8)
plt.xticks(np.arange(len(freq)) + 0.4, freq.keys())
plt.ylim(0, 1)
plt.show()
