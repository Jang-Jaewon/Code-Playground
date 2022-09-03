# Write your MySQL query statement below
SELECT MIN(ap.x - bp.x) AS shortest
FROM Point AS ap, Point AS bp
WHERE ap.x > bp.x;
