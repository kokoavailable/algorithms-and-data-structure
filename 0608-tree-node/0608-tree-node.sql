-- Write your PostgreSQL query statement below
-- 부모가 널이다. 루트. 
-- 날 부모로 삼는 노드가 없다. 리프
-- 날 부모로 삼는 노드가 있고 부모도 있다. 이너. 
-- 자식 컬럼만들기 날 p_id 로 삼는 것
SELECT 
    id,
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        WHEN id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree;