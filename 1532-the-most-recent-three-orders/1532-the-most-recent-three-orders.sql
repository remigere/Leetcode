# Write your MySQL query statement below
# select customer_name
# from 
# order by customer_name asc, customer_id asc, order_date desc

select c.name customer_name, t.customer_id, t.order_id, t.order_date
from
(
select *, dense_rank() over(partition by customer_id order by order_date desc) r
from orders
) t
natural join customers c
where t.r <= 3
order by customer_name asc, customer_id asc, order_date desc