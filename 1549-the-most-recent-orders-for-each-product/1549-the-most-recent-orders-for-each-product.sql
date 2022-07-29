# Write your MySQL query statement below
# select p.product_name, p.product_id, t.order_id, t.order_date
# from (select product_id, order_id, order_date,
#       rank() over(partition by product_id order by order_date) as date_rank
# from orders) as t
# natural join products p
# where t.date_rank = 1
# order by p.product_name, p.product_id, t.order_id

# select max(order_date) from orders group by product_id

select p.product_name, p.product_id, o.order_id, o.order_date
from orders as o
natural join products p
where o.order_date = (select max(order_date) from orders where product_id = p.product_id)
order by p.product_name, p.product_id, o.order_id