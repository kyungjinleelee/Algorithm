-- 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회
-- 이름이 같다면 보호 시간을 내림차순으로 정렬
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC
;