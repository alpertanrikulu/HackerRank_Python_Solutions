# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = list(map(int, input().split(" ")))

arr = list(input().split(" "))

A = set(list(input().split(" ")))
B = set(list(input().split(" ")))


happiness = 0

for i in range(n):
    if arr[i] in A:
        happiness += 1
    if arr[i] in B:
        happiness -= 1
        
print(happiness)
