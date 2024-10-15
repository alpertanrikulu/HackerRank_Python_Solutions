import numpy
numpy.set_printoptions(legacy="1.13")

s = list(map(int, input().split()))

print(numpy.eye(*s, k=0))
