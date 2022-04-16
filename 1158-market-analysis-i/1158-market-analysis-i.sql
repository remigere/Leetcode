# Write your MySQL query statement below
select user_id as buyer_id, join_date, 
    ifnull(count(order_date), 0) as orders_in_2019
from users left join orders on users.user_id = orders.buyer_id
AND year(order_date) = "2019"
group by user_id
