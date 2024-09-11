# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import atan, degrees

l1 = int(input())
l2 = int(input())

result = round(degrees(atan(l1/l2)))
print(f"{result}{chr(176)}")
