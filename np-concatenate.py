import numpy

N, M, P = list(map(int, input().split(" ")))

result1 = []
for i in range(N):
    arr = list(map(int, input().split(" ")))
    result1.append(arr)

result2 = []
for i in range(M):
    arr = list(map(int, input().split(" ")))
    result2.append(arr)
    
result = numpy.concatenate((result1, result2))
print(result)
