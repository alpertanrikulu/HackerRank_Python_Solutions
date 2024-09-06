# Enter your code here. Read input from STDIN. Print output to STDOUT

size = input().split(' ')

row = int(size[0])
column = int(size[1])

for i in range(row//2):
    print((".|."*i).rjust(column//2-1, "-") + ".|." + (".|."*i).ljust(column//2-1, "-"))

print("WELCOME".center(column, "-"))

for i in range(row//2, 0, -1):
    print((".|."*(i-1)).rjust(column//2-1, "-") + ".|." + (".|."*(i-1)).ljust(column//2-1, "-"))
