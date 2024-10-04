f = open('26(1).txt')
s = []
for i in f:
    k = list(map(int,i.split()))
    s.append(k)
pobeda = 0
dengi = 0
for i in s:
    pobeda += (i[1] - i[0]) // 25
    dengi += (i[1] - i[0]) * 2
print(pobeda,dengi)