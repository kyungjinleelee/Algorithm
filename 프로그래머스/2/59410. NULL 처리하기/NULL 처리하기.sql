SELECT ANIMAL_TYPE, 
    NVL(NAME, 'No name') AS NAME, -- 이름이 없는 동물의 이름은 "No name" 으로 표시
    SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID                -- ID 순으로 조회
;