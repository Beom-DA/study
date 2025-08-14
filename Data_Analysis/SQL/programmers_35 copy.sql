-- https://school.programmers.co.kr/learn/courses/30/lessons/59042



SELECT animal_id, O.name
    FROM animal_outs O
    LEFT JOIN animal_ins I
    USING (animal_id, animal_type)
    WHERE intake_condition IS null
    ORDER BY animal_id;