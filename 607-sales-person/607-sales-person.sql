# Write your MySQL query statement below
SELECT s.name
FROM Orders AS o JOIN Company AS c ON (o.com_id = c.com_id AND c.name = 'RED')
RIGHT JOIN SalesPerson AS s ON s.sales_id = o.sales_id
where o.sales_id is null
