if __name__ == '__main__':

    n = int(input())
    
    tupList = map(int, input().split(' '))
    t = tuple(tupList)
    print(hash(t))
