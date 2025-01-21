while True:
    a, b = map(int, input().split())  # 두 숫자 입력받기
    if a == 0 and b == 0:  # 종료 조건
        break
    
    if b % a == 0:  # 첫 번째 숫자가 두 번째 숫자의 약수
        print("factor")
    elif a % b == 0:  # 첫 번째 숫자가 두 번째 숫자의 배수
        print("multiple")
    else:  # 둘 다 아님
        print("neither")