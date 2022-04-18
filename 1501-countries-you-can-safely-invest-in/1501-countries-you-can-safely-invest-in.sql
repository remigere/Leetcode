# Write your MySQL query statement below
select co.name as country

from person p
join country co
on left(p.phone_number, 3) = co.country_code
join calls ca
on p.id in (ca.caller_id, ca.callee_id)
group by co.name
having avg(ca.duration) > (select avg(duration) from calls)
