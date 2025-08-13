-- https://school.programmers.co.kr/learn/courses/30/lessons/273712



SELECT item_id, item_name, rarity
    FROM item_info
    WHERE item_id NOT IN (
                SELECT item_id
                    FROM item_tree
                    WHERE item_id IN (SELECT parent_item_id FROM item_tree)    
    )
    ORDER BY item_id DESC;