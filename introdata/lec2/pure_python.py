def matmult(a,b):
    zip_b = zip(*b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
                             for col_b in zip_b] for row_a in a]

X = (xrange(100) for i in xrange(100))
Y = (xrange(1000) for i in xrange(100))

if __name__ == '__main__':
    run_res = matmult(X,Y)
