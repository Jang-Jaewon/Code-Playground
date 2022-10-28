# Write your MySQL query statement below
SELECT ad_id, IFNULL(ROUND(100 *SUM(IF(action = 'Clicked',1,0 )) / SUM(IF(action in ('Clicked', 'Viewed'),1,0)), 2),0) as ctr
FROM ads
GROUP BY ad_id
ORDER BY ctr desc, ad_id 