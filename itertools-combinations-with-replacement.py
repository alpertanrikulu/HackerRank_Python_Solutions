# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

inp = input().split(" ")
string = str(inp[0])
n = int(inp[1])
cList = list((combinations_with_replacement(string, n)))

rList = []
for i in cList:
    x = list(i)
    x.sort()
    rList.append("".join(x))

rList.sort()

for i in rList:
    print(i)
