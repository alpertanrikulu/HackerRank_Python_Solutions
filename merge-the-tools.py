def merge_the_tools(string, k):
    n = len(string)

    sList = []
    for i in range(0, n, k):
        sList.append(string[i:i+k])

    resultList = []
    for i in sList:
        setList = []
        for j in i:
            if j not in setList:
                setList.append(j)
        resultList.append("".join(setList))

    for i in resultList:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
