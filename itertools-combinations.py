# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

inp = input().split(" ")
string = str(inp[0])
n = int(inp[1])

for j in range(1, n+1):
    pList = list((combinations(string, j)))
    rList = ["".join(i) for i in pList]
    rList.sort()
    for i in rList:
        print(i)
