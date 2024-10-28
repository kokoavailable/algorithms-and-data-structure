-- Write your PostgreSQL query statement below
WITH RankedScore AS (
    select
        score,
        DENSE_RANK() over (ORDER BY score DESC) AS rank
    from
        Scores
)

select
    score,
    rank
from
    RankedScore
ORDER BY
    score DESC;