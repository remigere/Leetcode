# Write your MySQL query statement below
select name, if(distance, sum(distance), 0) as travelled_distance
from users left join rides on users.id = Rides.user_id
group by name
order by travelled_distance desc, name asc