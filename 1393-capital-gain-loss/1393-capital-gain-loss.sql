# Write your MySQL query statement below
select stock_name, sum(
    CASE 
        WHEN operation = "Buy" THEN -price
        ELSE price
    END
) as capital_gain_loss
from Stocks
group by stock_name
order by stock_name