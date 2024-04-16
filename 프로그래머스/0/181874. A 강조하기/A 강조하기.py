def solution(myString):
    answer = myString.lower()
    answer = answer.replace('a', 'A')
    return answer

# 일단 다 소문자로 바꿔 주고, 바꿔준거에서 a를 A로 바꿔주면 됨
# for문으로 순회할 때보다 오히려 더 쉽게 풀릴 때가 있다. 

        