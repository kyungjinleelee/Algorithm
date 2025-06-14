SELECT 
    COUNT(*) AS FISH_COUNT, 
    MAX(COALESCE(LENGTH, 10)) AS MAX_LENGTH, -- 10cm 이하의 물고기들은 NULL로 되어있기 때문에, CLALESCE를 통해 10cm로 계산되도록 함
    FISH_TYPE
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(COALESCE(LENGTH, 10)) >= 33
ORDER BY FISH_TYPE
;