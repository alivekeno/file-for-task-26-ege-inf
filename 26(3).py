f = open('26(3).txt')
n,s = map(int,f.readline().split())
defeat = n
zakaz = []
for i in f:
    k = list(map(int,i.split()))
    zakaz.append(k)
totalloss = 0
totaltime = 0
for i in zakaz:
    igr = (i[1] - i[0]) // 25
    loss = igr // defeat
    igr += loss
    totalloss += loss
    while loss >= defeat:
        igr += loss // defeat
        loss //= defeat
        totalloss += loss
    totaltime += igr * i[2]
srloss = totalloss // s
print(srloss,totaltime)