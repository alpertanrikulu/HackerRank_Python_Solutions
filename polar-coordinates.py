# Enter your code here. Read input from STDIN. Print output to STDOUT

from cmath import phase

cNumber = complex(input())
real = abs(cNumber)
img = phase(cNumber)

print(real)
print(img)
