-- https://leetcode.com/problems/article-views-i/

select DISTINCT author_id AS id
    FROM views
    WHERE author_id = viewer_id
    ORDER BY id;