# Write your MySQL query statement below
SELECT
    a.student_name AS member_A ,
    b.student_name AS member_B,
    c.student_name AS member_C
From SchoolA AS a, SchoolB AS b, SchoolC AS c
    WHERE (a.student_name <> b.student_name 
           and b.student_name <> c.student_name 
           and a.student_name <> c.student_name) 
    and (a.student_id <> b.student_id 
         and b.student_id <> c.student_id 
         and a.student_id <> c.student_id)