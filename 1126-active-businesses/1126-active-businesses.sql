# Write your MySQL query statement below
with t as
(
select event_type, avg(occurences) avgs
from events
group by event_type
)

select e.business_id
from events e
left join t
on e.event_type = t.event_type
where e.occurences > t.avgs
group by e.business_id
having count(*) > 1