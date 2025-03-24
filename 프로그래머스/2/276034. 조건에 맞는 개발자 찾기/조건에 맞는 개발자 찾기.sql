-- 두 테이블에는 공통되는 컬럼이 없기 때문에 JOIN이 아닌 카티션 곱을 수행해 가능한 모든 조합을 봐야함
SELECT  DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS D, SKILLCODES S
WHERE (D.SKILL_CODE & S.CODE) > 0
    AND S.NAME IN ("Python", "C#")
ORDER BY D.ID
;