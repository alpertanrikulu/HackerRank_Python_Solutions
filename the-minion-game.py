def minion_game(string):


    vowels = ['A', 'E', 'I', 'O', 'U']
    kevinScore = 0
    stuartScore = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevinScore += len(string) - i
        elif string[i] not in vowels:
            stuartScore += len(string) - i


    if kevinScore > stuartScore:
        print(f"Kevin {kevinScore}")
    elif kevinScore < stuartScore:
        print(f"Stuart {stuartScore}")
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
