-- Write your PostgreSQL query statement below

WITH 
    a2 AS (
        SELECT
            player_id,
            MIN(event_date) AS min_date
        FROM Activity
        GROUP BY player_id
    )
SELECT ROUND(
            COUNT(a1.player_id)::numeric / (SELECT COUNT(player_id) FROM a2),
            2
        ) AS fraction
FROM 
    Activity a1
JOIN 
    a2
ON 
    a1.player_id = a2.player_id
    AND a2.min_date = a1.event_date - INTERVAL '1 DAY';