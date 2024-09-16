# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

n = int(input())
columns = input().split(" ")
columns = [i for i in columns if i]
row = namedtuple("student", f"{columns[0]} {columns[1]} {columns[2]} {columns[3]}")
sum = 0

for i in range(n):
    c = input().split(" ")
    c0, c1, c2, c3 = [i for i in c if i]
    rowi = row(c0, c1, c2, c3)
    sum += int(rowi.MARKS)

print(sum/n)
