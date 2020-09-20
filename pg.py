# l = [i for i in range(1, 10)]
# l2 = []
# print(l)
# for i in l:
    # for j in l[1:]:
        # for k in l[2:]:
            # l2.append('%d*%d*%d' %(i, j, k))
            # l2.append(i*j*k)
# print(l2)
# a = int(input('number:'))
# if a in l2:
    # print('a in l2')
    # print(l2[l2.index(a)-1])

from itertools import product

l = 'abcd'
formula = "({a}*{b}*{c})+{d}"
ans = 211
for numbers in filter(lambda x: len(list(x)) == len(set(x)),
        product(*[range(10) for _ in l])):
# for numbers in product(*[range(10) for _ in l]):
    f = formula.format(**dict(zip(l, numbers)))
    if eval(f) == ans:
        print(f, "=", ans)
        break
