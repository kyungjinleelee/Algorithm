SELECT 
    COUNT(*) AS FISH_COUNT, 
    EXTRACT(MONTH FROM TIME) AS MONTH   -- TIME 컬럼에서 월을 숫자(1~12)로 추출
FROM
    FISH_INFO
GROUP BY 
    EXTRACT(MONTH FROM TIME)
ORDER BY 
    MONTH                               -- SELECT 다음에 실행되므로 별칭 사용 가능
;