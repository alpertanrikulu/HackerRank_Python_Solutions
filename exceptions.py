# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range(n):
    a, b = input().split(" ")
    
    try:
        print(round(int(a)/int(b)))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except Exception as e:
        print("Error Code:", e)
