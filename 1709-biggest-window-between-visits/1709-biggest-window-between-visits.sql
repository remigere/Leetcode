# Write your MySQL query statement below

with temp as
(
select user_id, 
    - datediff(visit_date, lead(visit_date, 1, '2021-01-01') over(partition by user_id order by visit_date)) as dif
from UserVisits
#order by user_id, visit_date
)


select distinct user_id, max(dif) as biggest_window
from temp t
group by user_id
order by user_id