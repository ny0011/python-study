def is_odd(number:int):

    number = int(number)
    if number % 2 == 0:
        return "EVEN"
    return "ODD"

print(is_odd("aa"))
print(is_odd(2))

assert is_odd(1) == "ODD"
assert is_odd(2) == "EVEN"


def average(number_list:list):
    sum_number = sum(number_list)
    return f"{(sum_number / len(number_list)):.2f}"
print("--------------------")
number_list = list(map(int, input("input number with separator : ,\n").split(",")))
print(number_list)
answer2 = average(number_list)
print(f"answer2 : {answer2}")

print("--------------------")
print("answer3 : int(input)으로 바꾸면 됨")

print("--------------------")
print("answer4 : 3번은 you need python")

print("--------------------")
print("answer5 : f1.close() 써주기")
