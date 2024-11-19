-- Write your PostgreSQL query statement below
select
    user_id,
    count(*) as followers_count
from
    Followers
GROUP BY
    user_id
ORDER BY
    user_id ASC;