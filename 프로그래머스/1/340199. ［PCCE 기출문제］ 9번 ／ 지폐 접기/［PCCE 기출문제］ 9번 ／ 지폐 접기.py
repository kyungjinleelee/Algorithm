def solution(wallet, bill):
    answer = 0

    wallet.sort()
    bill.sort()

    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        # 항상 긴 쪽을 반으로 접음
        if bill[0] >= bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
        
        # 접은 후 회전 가능 여부 확인
        bill.sort()  # 다시 정렬하여 작은 값이 앞에 오도록 함

    return answer