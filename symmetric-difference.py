# Enter your code here. Read input from STDIN. Print output to STDOUT

s1n = int(input())
s1 = set(map(int, input().split()))
s2n = int(input())
s2 = set(map(int, input().split()))

result = list(s1.difference(s2).union(s2.difference(s1)))
result.sort()

for i in range(len(result)):
    print(result[i])
