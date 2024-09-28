N = int(input())
cList = list(map(int, input().split()))

positives = all(i>0 for i in cList)
palindromic = any(all(str(i)[j] == str(i)[-(j+1)] for j in range(len(str(i)))) for i in cList)

print(all([positives, palindromic]))
