class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = {} 		# table이라는 빈 딕셔너리 선언
 
        for stone in stones:		  # stones의 각 돌에 대해 반복문을 수행 > 해당 돌이 table 딕셔너리에 이미 존재하는지 확인
            if stone not in table:		# 테이블 안에 stone인덱스가 없다면,
                table[stone] = 1		# 해당 인덱스 생성 후 1 넣어준다.
            else:
                table[stone] += 1		# 테이블 안에 stone인덱스가 있는데 같은 값이 들어왔다면, +1
                
 	      count = 0		# 변수 초기화
        for jewel in jewels:
            if jewel in table:			# table 안에 해당 인덱스를 골라서 count에 합산해줌
                count += table[jewel]
 
        return count
