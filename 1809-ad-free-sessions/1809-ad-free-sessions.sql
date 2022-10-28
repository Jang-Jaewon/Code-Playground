# Write your MySQL query statement below
SELECT p.session_id
FROM Playback AS p LEFT JOIN Ads AS ad
ON p.customer_id = ad.customer_id
AND ad.timestamp BETWEEN start_time and end_time
WHERE ad.customer_id IS NULL