def fastfib():
    prev = 1
    cur = 2
    s = 0
    while (cur < 1000000):
    	print(cur)
        s += cur
        prev += cur
        cur += prev
        cur += prev
        prev = cur - prev
    return s

def usualfib():
    prev = 1
    cur = 1
    s = 0
    while (cur < 1000000):
        if cur % 2 == 0: s += cur
        temp = cur + prev
        prev = cur
        cur = temp
    return s
   

print("Sum = "+str(fastfib()))
print("Usual sum = "+str(usualfib()))
