# Write your MySQL query statement below
select person1, person2, count(duration) as call_count, sum(duration) as total_duration
from (
select if(from_id > to_id, to_id, from_id) as person1,
    if(from_id > to_id, from_id, to_id) as person2,
    duration
    from Calls) as sub
group by person1, person2