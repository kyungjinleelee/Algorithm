def solution(numbers):
    # 숫자 단어와 숫자 매핑
    number_words = ["zero", "one", "two", "three", "four", 
                    "five", "six", "seven", "eight", "nine"]
    # 숫자 단어를 키, 숫자를 값으로 하는 딕셔너리 생성
    number_dict = {word: str(index) for index, word in enumerate(number_words)}
    
    # 결과를 담을 문자열 초기화
    result = ""
    temp_word = ""
    
    for char in numbers:
        temp_word += char
        if temp_word in number_dict:
            result += number_dict[temp_word]
            temp_word = ""
    
    return int(result)