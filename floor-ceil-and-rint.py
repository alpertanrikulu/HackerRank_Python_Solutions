import numpy
numpy.set_printoptions(legacy="1.13")

s = list(map(float, input().split(" ")))

result = numpy.array(s)

print(numpy.floor(result))
print(numpy.ceil(result))
print(numpy.rint(result))
