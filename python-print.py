if __name__ == '__main__':
    n = int(input())
    counter = 1
    result = []
    while counter < n+1:
        result.append(str(counter))
        counter += 1
        if counter > 150:
            break
        
    result = "".join(result)
    print(result)
