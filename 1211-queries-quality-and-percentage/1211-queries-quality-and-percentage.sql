select
    query_name,
    round(avg(rating::Numeric / position), 2) as quality,
    round(100.0 * sum(case when rating < 3 then 1 else 0 end) / count(*), 2) as poor_query_percentage
from
    queries
where query_name is not null
group by
    query_name;