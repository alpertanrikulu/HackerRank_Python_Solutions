# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(input())
dictionary = OrderedDict()
for i in range(n):
    s = input().split(" ")
    product = " ".join(s[0:len(s)-1])
    price = int(s[-1])
    if product in dictionary:
        dictionary[product] = int(dictionary[product]) + price
    else:
        dictionary[product] = price

for i in dictionary:
    print(i, dictionary[i])
