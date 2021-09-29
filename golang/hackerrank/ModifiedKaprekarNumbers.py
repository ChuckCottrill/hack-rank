// https://www.hackerrank.com/challenges/kaprekar-numbers/problem

def isKaprekar(x):
    square = x**2
    d = 10**len(str(x))
    l = square//d
    r = square%d
    return l+r==x

def kaprekarNumbers(p, q):
    kn=[]
    for x in range(p,q+1):
        if isKaprekar(x):
            kn.append(x)
    if kn:
        print(*kn)
    else:
        print("INVALID RANGE")


