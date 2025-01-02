n = []
for _ in range(28):
    n.append(int(input()))

stu_list = []
for i in range(1, 31): # 1 부터 30까지 리스트 만들기
    stu_list.append(i)
stu_set = set(stu_list)
n_set = set(n)

answer = sorted(stu_set - n_set)

for i in answer:
    print(i)