-- https://school.programmers.co.kr/learn/courses/30/lessons/164673



SELECT title, B.board_id, R.reply_id, R.writer_id, R.contents, DATE_FORMAT(R.created_date,'%Y-%m-%d') AS created_date
    FROM used_goods_board B
    LEFT JOIN used_goods_reply R
    USING (board_id)
    WHERE DATE_FORMAT(B.created_date, '%Y-%m') = '2022-10' AND reply_id IS NOT NULL
    ORDER BY R.created_date, title;