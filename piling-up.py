# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for i in range(n):
    N = int(input())
    s = list(map(int, input().split()))
    
    sList = s
    tempList = []
    result = "Yes"
    for i in range(len(sList)):
        both = [sList[0], sList[-1]]

        if not tempList:
            tempList.append(max(both))
            if max(both) == sList[0]:
                sindex = 0
            else:
                sindex = -1
            sList.pop(sindex)

        elif max(both) > tempList[-1]:
            result = "No"
            break
        else:
            tempList.append(max(both))
            if max(both) == sList[0]:
                sindex = 0
            else:
                sindex = -1
            sList.pop(sindex)
    print(result)
