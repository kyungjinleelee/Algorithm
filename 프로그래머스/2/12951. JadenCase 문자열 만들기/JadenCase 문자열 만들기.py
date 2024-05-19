def solution(s):
    answer = []
    words = s.split(' ')
    
    for word in words:
        if word:
            if word[0].isalpha():
                answer.append(word[0].upper() + word[1:].lower())
            else: 
                answer.append(word[0] + word[1:].lower())
        else:
            # 연속 공백
            answer.append('')
            
    return ' '.join(answer)