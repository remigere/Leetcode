# Write your MySQL query statement below
select c1.seat_id
from cinema c1
left join cinema c2 on c1.seat_id = c2.seat_id - 1
left join cinema c3 on c1.seat_id = c3.seat_id + 1
where c1.free and (c2.free or c3.free)
order by seat_id