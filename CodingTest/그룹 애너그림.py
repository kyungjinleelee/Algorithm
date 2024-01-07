import collections
from typing import List
# collections? 파이썬의 내장모듈로 이 모듈에서는 defaultdic을 지원함
#key의 개수를 세어야 하는 상황이나, list나 set의 항목을 정리해야하는 상황에 적절

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict : 존재하지 않는 key로 인한 에러 방지를 위해 사용 
        # 기본값 초기화 하지 않아도 자동으로 해주며 예외처리할 때 편하다.
        anagrams = collections.defaultdict(list)
        print(anagrams)

        for word in strs:
            # 정렬하여 딕셔너리에 추가 / 주어진 문자를 알파벳순으로 정렬하여 같은 애너그램을 key로 dic에 저장한다.
            anagrams[''.join(sorted(word))].append(word)
        print(anagrams)

        return list(anagrams.values()) 
