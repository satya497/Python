import collections
def stringmani():
    in_string = input("ENTER A STRING : ")
    d = collections.defaultdict(int)
    for c in in_string:
        d[c] += 1
    for c in sorted(d, key=d.get, reverse=True):
        print("The instances of ",c, "are : ", d[c])
    
    sortedstr = ''.join(sorted(in_string))
    print('\n')
    print("The sorted string is : ",sortedstr)
    print('\n')
                                                                    # for giving positions
    lsit1 = ([ch ,idx] for idx, ch in enumerate(in_string))
    for a in sorted(lsit1):
        print("the position of {} is : {}".format(a[0],a[1]+1))
    print('\n')

    str2 = sorted("".join(set(sorted(in_string))))
    for c in str2:
        print("the starting position of {} is {}".format(c,in_string.find(c)+1))
    array2 = list(str2)
    print('\n')
    print(array2)
stringmani()