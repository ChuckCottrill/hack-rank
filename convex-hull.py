

'''
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/lecture-videos/lecture-2-divide-conquer-convex-hull-median-finding/
starts at ??? 23:04
'''

points = [ ... ]

def ch(points):
    # divide
    n = len(points)
    pL = [:n//2]
    pR = [n//2:]
    # compute
    chL = ch_compute(pL)
    chR = ch_compute(pR)
    # combine
    ch = ch_combine(chL, chR)
    return ch

def two_finger():
    i = 1
    j = 1
    p = len(a)
    q = len(b)
    yi = a[i].y
    yj = b[j].y
    midpoint = y(i,j)
    while (y(i,j+1) > y(i,j)) or (y(i-1,j) > y(i,j)):
        if y(i,j+1): # move right finger #clockwise
            j = (j+1) % q
            yj = b[j].y
        else: # move left finger #counter-clockwise
            i = (i-1) % p
            yi = a[i].y
        midpoint = y(i,j)
    # found a[i],b[j] upper tangent
    return (a[i],b[j]) # as upper tangent

# two finger algorithm
def ch_combine(chL, chR):
    pL = find_minx(chL)
    pR = find_maxx(chR)

    # find upper tangent (max y)
    UT = two_finger(1,-1) # a[i], b[j]
    # find lower tangent (min y)
    LT = two_finger(-1,1) # a[k], b[m]
    ch = cut_paste( a, b, UT, LT )
    return ch

def cut_paste(...):
    #first link
    ch = (UT) # ( (a[i], b[j) )
    go down b list until you find a[k],b[m] (lower tangent)
    for bi in range(j,len(b)):
        ch.append(b[bi])
    for ai in range(i,len(a)):
        ch.append(a[ai])
    ch.append( LT ) #( (a[k], b[m) )
    return ch

def convex_hull(points):
    points = sorted(points) # sort by x-coordinates
    chL, chR = ch(points)



