# Write your MySQL query statement below
SELECT
    CASE 
    WHEN COUNT(*) > (SELECT COUNT(*) FROM California WHERE score >= 90) THEN 'New York University'
    WHEN COUNT(*) < (SELECT COUNT(*) FROM California WHERE score >= 90) THEN 'California University'
    ELSE 'No Winner' 
    END AS winner
FROM NewYork
WHERE score >= 90
