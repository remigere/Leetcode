# Write your MySQL query statement below
select seller_name
from seller left join orders
on seller.seller_id = orders.seller_id
AND year(sale_date) = "2020"
where order_id is null
order by seller_name