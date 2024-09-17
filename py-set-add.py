# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

country = list()
for i in range(n):
    country.append(input())

country = set(country)
print(len(country))
