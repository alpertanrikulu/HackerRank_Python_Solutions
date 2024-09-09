# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

inp = input().split(" ")
string = str(inp[0])
n = int(inp[1])

pList = list((permutations(string, n)))
rList = ["".join(i) for i in pList]
rList.sort()
for i in rList:
    print(i)
