if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    
    a = max(arr)
    liste = []
    for i in range(0, len(arr)):
        if arr[i] == a:
            liste.append(i)
    
    liste.sort(reverse=True)
    
    for i in liste:
        arr.pop(i)
        
    print(max(arr))
