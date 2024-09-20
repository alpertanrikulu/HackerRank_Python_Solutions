# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

d = deque()
n = int(input())

for i in range(n):
    s = input().split()
    command = s[0]
    parameter = s[1] if len(s) > 1 else False
    
    func = getattr(d, command, None)
    if parameter:
        func(parameter)
    else:
        func()
        
print(" ".join(d))
