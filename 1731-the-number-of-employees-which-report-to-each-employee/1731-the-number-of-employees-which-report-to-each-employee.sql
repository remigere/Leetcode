# Write your MySQL query statement below
select e.employee_id, name, 
(select sum(reports_to = e.employee_id) from employees) as reports_count, 
(select round(sum(if(reports_to = e.employee_id, age, 0)) / sum(reports_to = e.employee_id)) from employees) as average_age
from Employees as e
group by employee_id
having reports_count > 0
order by employee_id