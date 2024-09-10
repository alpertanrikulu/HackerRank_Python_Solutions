# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input()) # shoe number
sizeList = input().split(" ") # shoe sizes
sizeDict = dict(Counter(sizeList))
N = int(input()) #customer numbers

profit = 0
for i in range(N):
    size, price = input().split(" ")
    if (size in sizeList) and (sizeDict[size] > 0):
        sizeDict[size] -= 1
        profit += int(price)
print(profit)
