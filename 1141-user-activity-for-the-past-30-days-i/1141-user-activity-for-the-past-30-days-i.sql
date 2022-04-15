# Write your MySQL query statement below
select activity_date AS day, count(distinct user_id) as active_users
from Activity
where TO_DAYS("2019-07-27 ")  - 30 < TO_DAYS(activity_date) and TO_DAYS(activity_date) <= TO_DAYS("2019-07-27 ")
group by activity_date
order by activity_date