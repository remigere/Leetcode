# Write your MySQL query statement below
select prices.product_id, round(sum(units * price)/sum(units), 2) as average_price
from prices join unitssold
ON prices.product_id = unitssold.product_id
AND purchase_date Between start_date and end_date
group by product_id