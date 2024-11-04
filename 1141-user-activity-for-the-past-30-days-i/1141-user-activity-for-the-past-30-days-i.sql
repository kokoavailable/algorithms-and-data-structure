-- Write your PostgreSQL query statement below
select
    activity_date as day,
    COUNT(DISTINCT user_id) as active_users
from
    Activity
WHERE
    activity_date BETWEEN DATE '2019-06-28' AND DATE '2019-07-27'
Group by activity_date
    