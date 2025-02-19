n = int(input())
count = 0
num = 666

while True:
    if "666" in str(num): # 숫자에 '666'이 포함되었는지 확인
        count += 1
        # n번째 종말의 수를 찾았으면 출력 후 종료
        if count == n:
            print(num)
            break
    num += 1 # 다음 숫자로 이동