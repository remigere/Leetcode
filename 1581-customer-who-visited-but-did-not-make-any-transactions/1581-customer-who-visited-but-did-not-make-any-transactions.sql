# Write your MySQL query statement below
select customer_id, count(customer_id) as count_no_trans
from visits natural left join transactions
where amount is NULL
group by customer_id