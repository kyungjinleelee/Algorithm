SELECT
    it.ITEM_ID,
    ii.ITEM_NAME,
    ii.RARITY
FROM
    ITEM_TREE it
    JOIN ITEM_INFO pi ON it.PARENT_ITEM_ID = pi.ITEM_ID -- 부모 아이템 조인
    JOIN ITEM_INFO ii ON it.ITEM_ID = ii.ITEM_ID       -- 현 아이템 상세조인
WHERE
    pi.RARITY = 'RARE'
ORDER BY
    it.ITEM_ID DESC;