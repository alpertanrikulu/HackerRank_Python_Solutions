import numpy

s = list(map(int, input().split(" ")))

array = numpy.array(s)
result = numpy.reshape(array, (3,3))
print(result)
