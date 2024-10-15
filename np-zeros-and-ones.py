import numpy

liste = list(map(int, input().split(" ")))

r1 = numpy.zeros(liste, dtype = numpy.int32)
r2 = numpy.ones(liste, dtype = numpy.int32)
print(r1)
print(r2)
