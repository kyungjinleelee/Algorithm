-- FOOD_FACTORY 테이블에서 강원도에 위치한 식품공장의 공장 ID, 공장 이름, 주소 조회하기
-- 결과는 공장 ID를 기준으로 오름차순 정렬
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE "강원%"
ORDER BY FACTORY_ID
;