def solution(bin1, bin2):
    # 이진수를 십진수로 변환
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    
    # 두 숫자를 더하고, 결과를 이진수 문자열로 변환 (접두사 '0b' 제거)
    return bin(num1 + num2)[2:]