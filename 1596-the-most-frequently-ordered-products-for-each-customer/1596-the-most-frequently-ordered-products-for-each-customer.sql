# Write your MySQL query statement below
#select customer_id, product_id, product_name

select t.customer_id, t.product_id, p.product_name
from
    (
    select customer_id, product_id, rank() over(partition by customer_id order by count(*) desc) as counts
    from orders
    group by customer_id, product_id
    ) t
natural join products p
where t.counts = 1