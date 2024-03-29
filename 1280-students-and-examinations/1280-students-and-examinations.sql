# Write your MySQL query statement below
SELECT st.student_id, st.student_name, sb.subject_name, COUNT(ex.subject_name) as attended_exams
FROM Students as st
JOIN Subjects as sb
LEFT JOIN Examinations as ex
ON st.student_id = ex.student_id AND sb.subject_name=ex.subject_name
GROUP BY st.student_id, sb.subject_name
ORDER BY student_id, subject_name;