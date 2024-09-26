# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()
start = s.find('(') + 1
end = s.rfind(')')

print(eval(s[start:end]))
