if __name__ == '__main__':
    students = list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if len(students) == 0:
            lowest = score
            secondLowest = score
        else:
            if score < lowest and lowest != secondLowest:
                secondLowest = lowest
                lowest = score
            elif score < lowest and lowest == secondLowest:
                lowest = score
        students.append([name, score])
        
    names = list()
    for i in range(len(students)):
        if students[i][1] == secondLowest:
            names.append(students[i][0])
    names = sorted(names)
    for i in range(len(names)):
        print(names[i])
        
