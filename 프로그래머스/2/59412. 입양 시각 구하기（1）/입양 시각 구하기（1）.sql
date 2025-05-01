SELECT 
    HOUR(DATETIME) AS HOUR, -- DATETIME에서 입양 시간 추출
    COUNT(*) AS COUNT
FROM 
    ANIMAL_OUTS
WHERE 
    HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY
    HOUR(DATETIME)          -- 시간대 별 건수 집계
ORDER BY HOUR               -- 결과는 시간대 순으로 정렬
;
