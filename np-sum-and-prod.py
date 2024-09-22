import numpy

n = list(map(int, input().split()))

result = numpy.zeros(n)
for i in range(n[1]):
    row = numpy.array(list(map(int, input().split())))
    result[i] = row

resultSum = numpy.sum(result, axis=0)
resultProduct = numpy.prod(resultSum)
print(int(resultProduct))
