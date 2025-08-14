-- https://school.programmers.co.kr/learn/courses/30/lessons/59045



SELECT animal_id, animal_type, name
    FROM animal_ins I
    JOIN animal_outs O
    USING (animal_id, animal_type, name)
    WHERE (sex_upon_intake LIKE 'Intact%') 
    AND (sex_upon_outcome LIKE 'Neutered%' OR sex_upon_outcome LIKE 'Spayed%')
    ORDER BY animal_id