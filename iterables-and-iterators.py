# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

n = int(input())
s = "".join(input().split())
indice = int(input())

result = list(combinations(s, indice))
count = 0
length = len(result)
for i in range(length):
    if "a" in result[i]:
        count += 1

print(round(count/length, 4))
