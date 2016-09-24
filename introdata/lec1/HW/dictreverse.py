#coding=UTF-8
def dictreverse(d):
    for k in d.keys():
        v = d.pop(k)
        d[v] = k

d = {'a':1, 'b':2, 'c':3}
print(u'Исходный словарь:')
print(d)
dictreverse(d)
print(u'Перевернутый словарь:')
print(d)

