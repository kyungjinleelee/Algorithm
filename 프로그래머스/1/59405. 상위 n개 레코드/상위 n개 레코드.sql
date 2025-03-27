-- 동물 보호소에 가장 먼저 들어온 동물의 이름을 조회
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME ASC  -- 보호 시작일을 오름차순으로 정렬
FETCH FIRST 1 ROWS ONLY
;