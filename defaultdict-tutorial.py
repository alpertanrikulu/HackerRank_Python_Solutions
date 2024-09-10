# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = map(int, input().split(" "))
d = defaultdict(list)


for i in range(n):
    d["group A"].append(input())
    
groupB = list()
for i in range(m):
    d["group B"].append(input())
    

for i in d["group B"]:
    if i in d["group A"]:
        a = [str(indice+1) for indice, value in enumerate(d["group A"]) if value == i]
        a = " ".join(a)
        print(a)
    else:
        print(-1)
