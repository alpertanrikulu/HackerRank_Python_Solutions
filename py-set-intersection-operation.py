# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = input()
c1 = set(input().split())
n2 = input()
c2 = set(input().split())

result = c1.intersection(c2)
print(len(result))
