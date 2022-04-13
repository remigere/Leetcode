# Write your MySQL query statement below

SELECT 
    id AS Id, 
    CASE 
        WHEN tree.p_id is NULL
            THEN "Root"
        WHEN tree.id NOT IN (SELECT DISTINCT atree.p_id FROM tree atree WHERE atree.p_id IS NOT NULL)
            THEN "Leaf"
        ELSE "Inner"
    END AS Type
FROM
    Tree
order by Id
