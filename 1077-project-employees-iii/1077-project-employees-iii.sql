# Write your MySQL query statement below
SELECT project_id, employee_id
FROM project
JOIN employee
USING(employee_id)
WHERE (project_id, experience_years) in
(
    SELECT project_id, max(experience_years)
    FROM project
    JOIN employee
    USING(employee_id)
    group by project_id
)