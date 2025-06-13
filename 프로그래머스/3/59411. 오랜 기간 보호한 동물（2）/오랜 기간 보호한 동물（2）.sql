SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID 
ORDER BY O.DATETIME - I.DATETIME DESC    -- 보호 기간이 긴 순으로 조회
LIMIT 2                                  -- 보호 기간이 가장 길었던 동물 두 마리의 아이디
;