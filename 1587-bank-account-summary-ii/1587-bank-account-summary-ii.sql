# Write your MySQL query statement below
select name, sum(amount) balance
from users natural join transactions
group by account
having balance > 10000