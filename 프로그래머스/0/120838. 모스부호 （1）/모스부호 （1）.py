def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    # letter를 공백으로 분리하기
    split_letter = letter.split()
    
    # 각 모스 부호를 변환
    for i in split_letter:
        answer += morse[i]
    return answer

    # 이렇게 축약도 가능
    # decoded = ''.join(morse[code] for code in letter.split())