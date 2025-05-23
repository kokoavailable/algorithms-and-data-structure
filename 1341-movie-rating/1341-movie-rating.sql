WITH user_rating_count AS (
    SELECT 
        u.name,
        COUNT(*) as rated_cnt
    FROM MovieRating mr
    JOIN Users u ON mr.user_id = u.user_id
    GROUP BY u.user_id, u.name
    ORDER BY rated_cnt DESC, u.name ASC
    LIMIT 1
),

movie_avg_rating AS (
    SELECT 
        m.title,
        AVG(mr.rating) as avg_rating
    FROM MovieRating mr
    JOIN Movies m ON mr.movie_id = m.movie_id
    WHERE mr.created_at >= '2020-02-01' 
      AND mr.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title
    ORDER BY avg_rating DESC, m.title ASC
    LIMIT 1
)

SELECT name as results FROM user_rating_count
UNION ALL
SELECT title as results FROM movie_avg_rating;