# Write your MySQL query statement below

select co.name as country

from Calls as c

left join Person as p
on p.id in (c.caller_id, c.callee_id)

left join Country as co
on left(p.phone_number, 3) = co.country_code

group by co.name
having avg(duration) > (select avg(duration) from calls)

# SELECT
#  co.name AS country
# FROM
#  person p
#  JOIN
#      country co
#      ON SUBSTRING(phone_number,1,3) = country_code
#  JOIN
#      calls c
#      ON p.id IN (c.caller_id, c.callee_id)
# GROUP BY
#  co.name
# HAVING
#  AVG(duration) > (SELECT AVG(duration) FROM calls)