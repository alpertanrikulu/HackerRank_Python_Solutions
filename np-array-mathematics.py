import numpy

N, M = list(map(int, input().split(" ")))

A = list()
for i in range(N):
    A.append(list(map(int, input().split(" "))))

B= list()
for i in range(N):
    B.append(list(map(int, input().split(" "))))
    
A = numpy.array(A, numpy.int32)
B = numpy.array(B, numpy.int32)

print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(numpy.floor_divide(A,B))
print(numpy.mod(A,B))
print(numpy.power(A,B))
