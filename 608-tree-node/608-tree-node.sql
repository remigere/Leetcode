# Write your MySQL query statement below
SELECT 
    id AS Id, 
    CASE 
        WHEN tree.p_id is NULL
            THEN "Root"
        WHEN tree.id IN (SELECT atree.p_id FROM tree atree)
            THEN "Inner"
        ELSE "Leaf"
    END AS Type
FROM
    Tree
order by Id