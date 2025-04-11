SELECT COUNT(*) AS USERS     -- 총 몇 명인지 출력하기
FROM USER_INFO
WHERE AGE IS NULL   -- 나이 정보가 없는 회원
;