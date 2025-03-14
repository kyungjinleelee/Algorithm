-- 진료과가 흉부외과이거나 일반외과인 의사의 이름, 의사 ID, 진료과, 고용일자 조회
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
-- 고용일자를 기준으로 내림차순 정렬, 고용일자가 같다면 이름을 기준으로 오름차순 정렬
ORDER BY HIRE_YMD DESC, DR_NAME
;