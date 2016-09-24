#coding=UTF-8
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
    
with open('input.txt', 'r') as f:
    for line in f:
        for ch in line.decode('utf8'):
            if ch.isalnum() : total += 1
            if ch in count.keys(): count[ch] += 1

print('Частотность русских гласных в тексте:')
print_freq(count, total)
