# Write your MySQL query statement below
SELECT Person.FirstName, Person.LastName, Address.City, Address.State 
From Person LEFT JOIN Address on Person.PersonId = Address.PersonId;
