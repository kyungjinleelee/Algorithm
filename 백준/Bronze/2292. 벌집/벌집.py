n = int(input())

if n == 1:
    print(1)
else:
    layer = 1  # 몇 번째 껍질인지
    max_num = 1  # 해당 껍질의 최댓값

    while max_num < n:
        max_num += 6 * layer  # 다음 껍질의 최댓값
        layer += 1

    print(layer)