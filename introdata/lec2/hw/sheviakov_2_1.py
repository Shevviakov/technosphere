def f1(x):
    return (x*(x>0))+(0.01*x*(x<=0))

def f2(x, sigma):
    try:
        y = np.random.normal(loc=0.0, scale=sigma, size=len(x))
    except TypeError:
        y = np.random.normal(loc=0.0, scale=sigma)
    print y
    return (x+y)*((x+y)>0)
