
'''
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/lecture-videos/lecture-2-divide-conquer-convex-hull-median-finding/
starts at 58:04

Recurrence:
T(n) = { O(1) for n <= 140
       { T(ceil[n/5] + ceil(7n/10+6] + \Theta(n)
'''

def median(L):
    '''
    L = sort(L)
    return median(L)
    '''
    n = len(L)
    if n > 1:
        L = sorted(L)
    return L[n//2]

def pick_x(S):
    '''
    pick x in clever way
    arrange S into 2D array [n//5,5]
    sort columns
    find median of medians
    How many elements are guaranteed > x?
    Half of the ceil(n/5] contribute at least 3 elements > x
    (except one group having less than 5 elements, and 1 group that contains x)
    Half of the floor(n/5] contribute at least 3 elements < x
    At least 3*(ceil[n/10]-2) elements > x
    At least 3*(ceil[n/10]-2) elements < x
    '''
    M = [ median(S[i*5:(i+1)*5]) for i in range(len(S)//5) ]
    M = sorted(M)
    return M[len(M)//2]

def select_rank(S,i):
    # i is rank
    n = len(S)
    # pick x in S
    xi = random(n)
    # B = { y in S | y < x } # elements < x
    B = [ y for y in S if y < x ]
    # C = { y in S | y > x } # elements > x
    C = [ y for y in S if y > x ]
    # graphically, [ ... B ... | x | ... C ... ]
    # compute k = rank(x)
    # p = len(B) # |B| = p = k-1 elements
    # q = len(C) # |C| = q = n - k elements
    # k = rank(x) = |B| + 1
    k = len(B) + 1 # k = p + 1 = |B| + 1 elements
    if k > i:
        return select_rank(B,i)
    if k < i:
        return select_rank(B,i-k)
    # k == i
    return x

def rank_find(S,i):
    x = select_rank(S,i)
    return x

def median_find(S):
    n = len(S)
    return rank_find(S,n/2)

