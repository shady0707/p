def func(a, b):
    a1 = [int(i) for i in a]
    b1 = [int(j) for j in b]
    c1 = []
    #c1 = [int(i) for i in str(int(a) + int(b))]
    if len(a1)>len(b1):
        a1, b1 = b1, a1
    a1 = [0] * (len(b1)-len(a1))+a1
    print(a1)


    for i, j in zip(a1, b1):
        c1.append(i + j)
    
    for i in range(len(c1)-1, 0, -1):
        jw = c1[i] // jz #这一步把列表的这一项jz的倍数取了出来放在jw。
        c1[i] %= jz #这一步把列表的这一项的个位数取了出来然后放在了这一位。
        c1[i-1] += jw

    if c1[0] >= jz:
        c1.insert(0, c1[0] // jz)
        c1[1] %= jz
    return ''.join([str(i) for i in c1])


jz = 10
print(func('34', '157'))