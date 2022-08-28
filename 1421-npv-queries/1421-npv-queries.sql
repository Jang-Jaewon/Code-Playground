# Write your MySQL query statement below
SELECT q.id, q.year, COALESCE(n.npv, 0) AS npv
from npv AS n RIGHT JOIN queries AS q
ON n.id = q.id AND n.year = q.year