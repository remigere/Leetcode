# Write your MySQL query statement below
SELECT employee_id 
FROM Employees 
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
OR employee_id is NULL

UNION 

SELECT employee_id 
FROM Salaries 
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
OR employee_id is NULL

ORDER BY 1 ASC