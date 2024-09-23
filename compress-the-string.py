# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

s = list(input())

result = [(list(g).count(k), int(k)) for k, g in groupby(s)]

for i in result:
    print(i, end=" ")
