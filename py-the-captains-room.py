# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())
entries = input().split()

entrySet = set(entries)

for i in entrySet:
    try:
        entries.remove(i)
        entries.remove(i)
    except:
        print(i)
        break
