# Write your MySQL query statement below
select t1.id as p1, t2.id as p2, abs(t1.y_value - t2.y_value) * abs(t2.x_value - t1.x_value) as area
from points as t1 cross join points as t2
where t1.x_value != t2.x_value and t1.y_value != t2.y_value and t1.id < t2.id
order by area desc, p1 asc, p2 asc