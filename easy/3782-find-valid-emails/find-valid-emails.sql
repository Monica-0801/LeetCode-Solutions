# Write your MySQL query statement below
select * from Users where email REGEXP '^[a-z0-9]+(\_[a-z0-9]+)*@[a-z]+\\.com$' order by user_id;