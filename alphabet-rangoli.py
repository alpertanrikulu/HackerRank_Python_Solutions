def print_rangoli(size):
    width = ((size*2)-1)+ ((size*2)-2)
    charList = [chr(i) for i in range(97, 123)]
    
    rowList = []
    for i in range(size):
        a = [j for j in charList[size-1: size-i-1: -1]]
        b = [k for k in charList[size-i-1: size]]
        a += b
        rowList.append("-".join(a).center(width, "-"))
    

    rowList2 = []
    for i in range(len(rowList)-2, -1, -1):
        rowList2.append(rowList[i])

    rowList += rowList2

    
    rowList = "\n".join(rowList)
    print(rowList)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
