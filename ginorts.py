# Enter your code here. Read input from STDIN. Print output to STDOUT

s = list(input())

lowerCase = []
upperCase = []
numerics = []

for i in s:
    if ord(i) > 96:
        lowerCase.append(i)
    elif ord(i) > 60:
        upperCase.append(i)
    else:
        numerics.append(int(i))
        
lowerCase.sort()
upperCase.sort()
numerics.sort()

evenNumbers = []
oddNumbers = []
for i in numerics:
    if i % 2 == 0:
        evenNumbers.append(str(i))
    else:
        oddNumbers.append(str(i))

result = "".join(lowerCase + upperCase + oddNumbers + evenNumbers)
print(result)
