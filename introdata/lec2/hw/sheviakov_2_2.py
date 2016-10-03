import mmh3

def hashing_trick(input_dict, bits):
    x = {}
    for f in input_dict:
        s = ''
        s = s.join((str(f),':',str(input_dict[f])))
        h = mmh3.hash(s) % (2**bits)
        print ('hash: '+str(h))
        try:
            x[h] += 1
        except KeyError:
            x[h] = 1
    return x
