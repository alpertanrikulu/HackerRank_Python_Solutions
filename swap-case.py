def swap_case(s):
    
    caseList = list(s)
    i = 0
    while i < len(caseList):
        if caseList[i].isupper():
            caseList[i] = caseList[i].lower()
        else:
            caseList[i] = caseList[i].upper()
            
        i +=1
    
    return "".join(caseList)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
