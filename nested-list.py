if __name__ == '__main__':
    
    scores = []
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        scores.append(score)
        students.append([name, score])
        
    
    setScores = list(set(scores))
    setScores.sort()
    ademandedScore = setScores[1]
    demandedStudents = [i[0] for i in students if i[1] == ademandedScore]
    demandedStudents.sort()
    for i in demandedStudents:
        print(i)
