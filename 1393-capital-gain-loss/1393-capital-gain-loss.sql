# Write your MySQL query statement below
select stock_name, sum(profit) as capital_gain_loss
from
    (select stock_name, IF(operation = "Buy", - price, price) as profit
     from Stocks) as s
group by stock_name
order by stock_name