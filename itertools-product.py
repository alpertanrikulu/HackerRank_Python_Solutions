i1 = input()
i2 = input()

i1 = i1.split(" ")
i2 = i2.split(" ")

i1 = list(map(int, i1))
i2 = list(map(int, i2))
pList = []
for i in i1:
    for j in i2:
        a = f'({i}, {j})'
        pList.append(a)

result = " ".join(pList)
print(result)
