-- # 본인이 리퀘스터든 어셉터든 하나의 로우라도 속해있으면 친구로 친다.
-- # 모든 해당 로우를 반환하고, id를 함꼐 반환한다.


WITH all_ids AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
),
friend_counts AS (
    SELECT id, COUNT(*) AS num
    FROM all_ids
    GROUP BY id
)
SELECT id, num
FROM friend_counts
ORDER BY num DESC
LIMIT 1;