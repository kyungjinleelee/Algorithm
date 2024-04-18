def solution(num_list):
    for num in num_list:
        if num_list[-1] > num_list[-2]:
            num_list.append(num_list[-1] - num_list[-2])
            break
        else:
            num_list.append(num_list[-1] * 2)
            break
    return num_list