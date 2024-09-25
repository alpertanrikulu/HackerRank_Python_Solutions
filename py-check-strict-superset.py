# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(input().split())
n = int(input())

result = True
for i in range(n):
    B = set(input().split())
    if not B.issubset(A):
        result = False
        break
        
print(result)
