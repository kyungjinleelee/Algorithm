def solution(arr):
    x = 0
    while True:
        transformed_arr = []
        for i in arr:
            if i % 2 == 0 and i >= 50:
                transformed_arr.append(i // 2)
            elif i % 2 != 0 and i < 50:
                transformed_arr.append(i * 2 + 1)
            else:
                transformed_arr.append(i)
                
        if arr == transformed_arr:
            return x
        arr = transformed_arr
        x += 1
    return x