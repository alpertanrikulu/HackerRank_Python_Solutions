import numpy

def arrays(arr):
    result = []
    for i in range(len(arr)-1,-1,-1):
        result.append(float(arr[i]))
    a = numpy.array(result, float)
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
