# Write your MySQL query statement below
select dept_name, count(s.dept_id) as student_number
from department
left join student s
using (dept_id)
group by dept_id
order by student_number desc, dept_name asc