def dictreverse(d):
    for k in d.keys():
        v = d.pop(k)
        d[v] = k

d = {'a':1, 'b':2, 'c':3}
print(d)
dictreverse(d)
print(d)

