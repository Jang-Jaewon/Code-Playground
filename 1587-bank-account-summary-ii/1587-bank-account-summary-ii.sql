# Write your MySQL query statement below
SELECT name, SUM(amount) AS balance
FROM Users AS U
JOIN Transactions AS T
ON U.account = T.account
GROUP BY name
HAVING SUM(amount) > 10000