SELECT
    MONTH(START_DATE) AS MONTH,
    CAR_ID,
    COUNT(HISTORY_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    START_DATE >= '2022-08-01' AND START_DATE <= '2022-10-31'
    AND CAR_ID IN (SELECT CAR_ID
                   FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                  WHERE START_DATE >= '2022-08-01' AND START_DATE <= '2022-10-31'
                  GROUP BY CAR_ID
                  HAVING COUNT(HISTORY_ID) >= 5)
GROUP BY MONTH, CAR_ID
HAVING RECORDS >= 1     -- 총 대여횟수가 0인 경우는 제외하기
ORDER BY MONTH, CAR_ID DESC
;
    