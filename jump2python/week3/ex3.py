def print_answer(answer, quest_number):
    print(f"{answer[0]}")

    for i in range(1,quest_number):
        print(f"A{i}. {answer[i]}")


def three_multiple_one():
    max_num = 1000
    start=1
    answer = 0
    while (max_num >= start):
        if start % 3 == 0:
            answer += start
        start +=1
    return answer

def three_multiple_two():
    max_num = 1000
    start = 3
    answer = 0
    while(max_num >= start):
        answer += start
        start+=3
    return answer

def three_multiple_three():
    return (3+999)*333//2

def print_star():
    s = "\n"
    for i in range(1,5):
        s +="*"*i + "\n"        
    s+="*"*5
    return s

def print_hundread():
    s = "\n"
    for i in range(1,101):
        s+=f"{i:3d}\n"
    return s

def average_grade():
    grades = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    total_grade=0
    for grade in grades:
        total_grade+=grade
    return total_grade/len(grades)

if __name__ == "__main__":
    quest_number = 1+6
    answer = dict()
    answer[0] = "example 3."

    answer[1] = "shirt"
    answer[2] = [three_multiple_one(), three_multiple_two(), three_multiple_three()]
    answer[3] = print_star()
    answer[4] = print_hundread()
    answer[5] = average_grade()
    numbers = [1,2,3,4,5]
    answer[6] = '[ n*2 for n in numbers if n % 2 == 1 ]'

    print_answer(answer,quest_number)



