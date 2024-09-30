cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        result = []
        return result
    elif n == 1:
        result = [0]
        return result
    else:
        result = [0, 1]
        for i in range(0, n-2):
            result.append(result[i] + result[i+1])
        return result
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
