-- https://school.programmers.co.kr/learn/courses/30/lessons/273711


select i.ITEM_ID, i.ITEM_NAME, i.RARITY
    from ITEM_INFO i
    join ITEM_TREE t on i.ITEM_ID = t.ITEM_ID
    where PARENT_ITEM_ID in (SELECT ITEM_ID FROM ITEM_INFO WHERE RARITY = 'RARE')
    order by ITEM_ID desc;