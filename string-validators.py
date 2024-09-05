if __name__ == '__main__':
    s = input()
    s = list(s)
    
    alnum = False
    alpha = False
    digit = False
    loweCase = False
    upperCase = False
    for i in s:
        if i.isalnum():
            alnum = True
        if i.isalpha():
            alpha = True
        if i.isdigit():
            digit = True
        if i.islower():
            loweCase = True
        if i.isupper():
            upperCase = True
    
    print(alnum)
    print(alpha)
    print(digit)
    print(loweCase)
    print(upperCase)
