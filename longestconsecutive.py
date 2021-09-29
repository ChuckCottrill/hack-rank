

"""
Part 1
------
[1,1] => 2
[] => 0
[0] => 0
[1,1,1,0,1,1,0,1] => 3
[1,0,1,1,0,1,1,1] => 3
"""

def longestConsecutive(list):
    """ assume list is a list """
    if len(list) == 0:
        return 0
    longest = 0
    currentlen = 0
    for element in list:
        if element == 1:
            currentlen += 1
            if currentlen > longest:
                longest = currentlen
        else:
            currentlen = 0
    return longest

testcases = [
    ([1,1], 2),
    ([], 0),
    ([0], 0),
    ([1,1,1,0,1,1,0,1], 3),
    ([1,0,1,1,0,1,1,1], 3)
]

for tc in testcases:
    result = longestConsecutive(tc[0])
    if result == tc[1]:
        print("ok",tc[0])
    else:
        print("fail",tc[0],result)
print("")
     
    
"""
Part 2
------
[1,1] => 2
[1,0,1] => 2
[1,0,0,1] => 1

[1,0,1,1,0,1,1,1] => 5
[1,1,1,0,1,1,0,1] => 5
"""

def longestConsecutive2(list,missing=1):
    """ assume list is a list
    consecutive missing """
    if len(list) == 0:
        return 0
    longest = 0
    currentlen = 0
    sublists = []
    for element in list:
        if element == 1:
            allowmiss = missing
            currentlen += 1
            if currentlen > longest:
                longest = currentlen
        else:
            if currentlen > 0:
                sublists.append(currentlen)
                currentlen = 0
            allowmiss -= 1
            if allowmiss < 0:
                sublists.pop() #too much gap, drop
    if currentlen > 0:
        sublists.append(currentlen)
    # need two largest adjacent in sublist...
    if len(sublists) == 0:
        return 0
    if len(sublists) == 1:
        return sublists[0]
    prev = sublists[0]
    longest = 0
    largest = [0 for x in sublists]
    for index,value in enumerate(sublists[1:]):
        largest[index] = prev + value
        prev = value
        if longest < largest[index]:
            longest = largest[index]
    return longest

testcases = [
    ([1,1], 2),
    ([1,0,1], 2),
    ([1, 0, 0, 1], 1),
    ([1,0,1,1,0,1,1,1], 5),
    ([1,1,1,0,1,1,0,1], 5),
]

for tc in testcases:
    result = longestConsecutive2(tc[0],1)
    if result == tc[1]:
        print("ok",tc[0])
    else:
        print("fail",tc[0],result)
print("")
        
        
"""
Part 3
------

([1,0,0,1], 1) => 1
([1,0,1,1,0,1,1,1], 1) => 5
([1,0,0,1], 2) => 2
([1,0,1,1,0,1,1,1], 2) => 6
"""

def longestConsecutive3(list,missing=1):
    """ assume list is a list
    budget missing """
    if len(list) == 0:
        return 0
    longest = 0
    # print(range(len(list)-1))
    starts = [ x for x in range(len(list)) ]
    # print(starts)
    for sindex in starts:
        currentlen = 0
        allow = missing
        # print(sindex)
        # print(sindex,list[sindex:])
        for element in list[sindex:]:
            if element == 1:
                currentlen += 1
            else:
                allow -= 1
                if allow < 0:
                    break
        starts[sindex] = currentlen
        if currentlen > longest:
            longest = currentlen
        # print(sindex,currentlen)
    return longest

testcases = [
    ([1,0,0,1], 1, 1),
    ([1,0,1,1,0,1,1,1], 1, 5),
    ([1,0,0,1], 2, 2),
    ([1,0,1,1,0,1,1,1], 2, 6),
]

for tc in testcases:
    # print(tc[0],tc[1],tc[2])
    result = longestConsecutive3(tc[0],tc[1])
    if result == tc[2]:
        print("ok",tc[0])
    else:
        print("fail",tc[0],result)
print("")


