# Write your MySQL query statement below
select s2.stock_name, sum(s2.profit) as capital_gain_loss
from
    (select s.stock_name, IF(s.operation = "Buy", - s.price, s.price) as profit
     from Stocks s) as s2
group by s2.stock_name
order by s2.stock_name