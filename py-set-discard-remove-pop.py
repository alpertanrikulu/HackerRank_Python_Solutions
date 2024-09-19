n = int(input())
s = set(map(int, input().split(" ")))

N = int(input())


for i in range(N):
    given = input().split(" ")
    command = given[0]
    parameter = given[1] if len(given) > 1 else None
    
        

    func = getattr(s, command, None)

    if callable(func):
        if len(given) > 1:
            func(int(parameter))
        else:
            func()
        
result = sum(s)
print(result)
