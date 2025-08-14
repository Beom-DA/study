-- https://school.programmers.co.kr/learn/courses/30/lessons/144856



SELECT author_id, author_name, category, SUM(price * sales) AS total_sales
    FROM book
    JOIN author
    USING (author_id)
    JOIN book_sales
    USING (book_id)
    WHERE sales_date BETWEEN '2022-01-01' AND '2022-01-31'
    GROUP BY author_id, author_name, category
    ORDER BY author_id, category DESC;