f = open('26(2).txt')
n,s = map(int,f.readline().split())
teksumm = 0
zakaz = []
for s in f:
    s = list(map(int,s.split()))
    zakaz.append(s)
zakaz.sort()
time = 0
i = 0
num = 0
while teksumm < n:
    if zakaz[i][3] >= 15:
        kolvoigr = (zakaz[i][2] - zakaz[i][1]) // 25
        time += kolvoigr * zakaz[i][3]
        teksumm += (zakaz[i][2] - zakaz[i][1]) * 3
        num += 1
    i += 1
time //= 60
print(time,num)