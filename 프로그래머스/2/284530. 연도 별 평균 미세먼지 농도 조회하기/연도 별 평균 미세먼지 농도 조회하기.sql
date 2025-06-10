SELECT
    YEAR(YM) AS YEAR,                   -- 연도 값만 추출
    ROUND(AVG(PM_VAL1), 2) AS 'PM10',   -- 소수 셋째 자리에서 반올림
    ROUND(AVG(PM_VAL2), 2) AS 'PM2.5'   -- 소수 셋째 자리에서 반올림
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY 1
ORDER BY 1
;