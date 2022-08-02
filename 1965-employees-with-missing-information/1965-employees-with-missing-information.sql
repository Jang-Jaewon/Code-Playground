# Write your MySQL query statement below
SELECT R.employee_id 
FROM
    (
        SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
        UNION
        SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id)
    ) AS R
WHERE R.salary IS NULL OR R.name IS NULL
ORDER BY employee_id;
