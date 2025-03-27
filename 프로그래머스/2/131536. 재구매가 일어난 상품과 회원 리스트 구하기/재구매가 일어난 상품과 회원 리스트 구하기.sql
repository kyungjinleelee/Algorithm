-- 재구매한 회원 ID와 재구매한 상품 ID를 출력하기
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID        -- 같은 USER_ID, PRODUCT_ID 조합별로 그룹화
HAVING COUNT(*) > 1                 -- 한 번 이상 구매한 경우만 필터링
ORDER BY USER_ID, PRODUCT_ID DESC   -- USER_ID 기준 오름차순, 동일 USER_ID 내에서 PRODUCT_ID 기준 내림차순 정렬
;
