-- 175. Combine Two Tables - Easy
-- Write an SQL query to report the first name, last name, city, and state of each person in the Person table.
-- If the address of a personId is not present in the Address table, report null instead.Return the result table 
-- in any order.

-- Write your MySQL query statement below

SELECT
  a.firstName,
  a.lastName,
  b.city,
  b.state
FROM
  Person a
  LEFT JOIN Address b on a.personID = b.personID