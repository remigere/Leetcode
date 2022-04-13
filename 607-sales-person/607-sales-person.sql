# Write your MySQL query statement below
SELECT DISTINCT SalesPerson.name
FROM SalesPerson
Where SalesPerson.sales_id NOT IN 
    (SELECT DISTINCT orders.sales_id
    FROM Orders
    WHERE orders.com_id = (SELECT Company.com_id FROM Company WHERE Company.name = "RED"))