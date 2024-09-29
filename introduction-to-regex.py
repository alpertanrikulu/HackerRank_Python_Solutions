# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

for i in range(N):
    s = input()
    
    if len(s) == 1:
        print(False)
        continue
    try:
        r = float(s)
        print(True)
    except:
        print(False)
