SELECT I.NAME, I.DATETIME                                   -- 동물 이름과 보호 시작일을 조회
FROM ANIMAL_INS I
LEFT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID    -- left join을 통해 모든 입소 동물 정보를 가져옴
WHERE O.ANIMAL_ID IS NULL                               -- 입양 기록이 없는 동물만 필터링
ORDER BY I.DATETIME
LIMIT 3
;
