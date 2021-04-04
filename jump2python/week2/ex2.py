quest_number = 1+12
answer = dict()

answer[0] = "example 2."
answer[1] = (80+75+55)/3
answer[2] = 13%2
pin = "881120-1068234"
answer[3] = f"pin birthday : {pin[:6]}, id : {pin[7:]} "
answer[4] = f"Male : 1, Female : 2, my gender : {pin[7]}"

q5 = "a:b:c:d"
answer[5] = q5.replace(":","#")
q6 = [1, 3, 5, 4, 2]
q6.sort()
q6.reverse()
answer[6] = q6
q7 = ['Life', 'is', 'too', 'short']
answer[7] = ' '.join(q7)

answer[8] = (1,2,3) + (4,)
answer[9] = '\n3번 a[[1]] = \'python\', TypeError: unhashable type: list가 나온다. key로 hashable을 써야 함\n'+'a[{1}]=1, a[{1:12}]=1도 type error지만 a[(1)]=1은 가능'
a = {'A':90, 'B':80, 'C':70}
answer[10] = a.pop('B')
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
answer[11] = list(set(a))
answer[12] = '[1,4,3]으로 a와 같다. a=b=[1,2,3]에서 값복사가 아니라 address copy. '

print(f"{answer[0]}")
print(f"A1. {answer[1]:.2f}")

for i in range(2,quest_number):
    print(f"A{i}. {answer[i]}")
