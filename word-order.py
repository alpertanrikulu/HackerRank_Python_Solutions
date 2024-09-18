# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

sDict = {}
for i in range(n):
    s = input()
    if s not in sDict:
        sDict[s] = 1
    else:
        sDict[s] = int(sDict[s]) + 1

resultList = []
for i in sDict:
    resultList.append(str(sDict[i]))
    
    
print(len(resultList))
print(" ".join(resultList))
