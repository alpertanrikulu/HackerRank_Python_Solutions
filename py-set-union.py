# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(input())
c1 = set(input().split())

n2 = int(input())
c2 = set(input().split())

result = c1.union(c2)
print(len(result))
