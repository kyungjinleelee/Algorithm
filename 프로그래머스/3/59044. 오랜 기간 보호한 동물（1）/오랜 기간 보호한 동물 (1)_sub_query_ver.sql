SELECT NAME, DATETIME       -- 동물 이름과 보호 시작일을 조회
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (    -- 입양 안 된 동물만 필터링
    SELECT ANIMAL_ID
    FROM ANIMAL_OUTS
)
ORDER BY DATETIME
LIMIT 3
;
