SELECT 
    B.TITLE,        -- 게시글 제목
    B.BOARD_ID,     -- 게시글 ID
    R.REPLY_ID,     -- 댓글 ID
    R.WRITER_ID,    -- 댓글 작성자 ID
    R.CONTENTS,     -- 댓글 내용
    TO_CHAR(R.CREATED_DATE, 'YYYY-MM-DD') AS CREATED_DATE  -- 댓글 작성일
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_REPLY R
    ON B.BOARD_ID = R.BOARD_ID  -- 게시글과 댓글을 JOIN
WHERE TO_CHAR(B.CREATED_DATE, 'YYYY-MM') = '2022-10' --  작성일은 DATE 타입이기 때문에 LIKE 사용 불가 (LIKE는 VARCHAR 타입에서만 동작함)
ORDER BY R.CREATED_DATE, B.TITLE
;