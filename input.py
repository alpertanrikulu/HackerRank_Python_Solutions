# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k = list(map(float, input().split()))

P = input()

def func(P):
    return lambda x: eval(P)
resultFunc = func(P)
result = resultFunc(x)

if k == result:
    print(True)
else:
    print(False)
