# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range(T):
    nA = int(input())
    A = set(input().split())
    
    nB = int(input())
    B = set(input().split())
    
    result = A.issubset(B)
    print(result)
