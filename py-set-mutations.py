n = int(input())
s = set(input().split())

N = int(input())
for i in range(N):
    command, sn = input().split()
    R = set(input().split())
    func = getattr(s, command, None)
    if callable(func):
        func(R)
        
s = set(map(int, s))
print(sum(s))
