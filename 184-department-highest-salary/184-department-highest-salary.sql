# Write your MySQL query statement below
select 
    d.name as Department, 
    e.name as Employee, 
    e.salary as Salary
from
    employee e
    join Department d
    on e.departmentId = d.id
and
    (e.DepartmentId, e.salary) in
    (select DepartmentId, max(salary)
    from Employee
    group by DepartmentId)