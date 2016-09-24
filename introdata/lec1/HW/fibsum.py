def fib():
    prev = 1
    cur = 2
    s = 0
    while (cur < 1000000):
        s += cur
        prev += cur
        cur += prev
        cur += prev
        prev = cur - prev
    return s
print("Sum = "+str(fib()))
