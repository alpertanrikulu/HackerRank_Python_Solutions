def print_formatted(number):
    space = str(bin(number))
    space = len(space)-1
    for i in range(1, number+1):
        print(f"{i:>{space-1}}{oct(i)[2:]:>{space}}{hex(i)[2:].upper():>{space}}{bin(i)[2:]:>{space}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
