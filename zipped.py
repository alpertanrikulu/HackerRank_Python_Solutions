# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = list(map(int, input().split()))

marks = []
for i in range(X):
    a = list(map(float, input().split()))
    marks.append(a)
    
zippedList = list(zip(*marks))

for i in zippedList:
    print(sum(i)/X)
