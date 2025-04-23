select(
select 
distinct(salary) 
FROM Employee
order by salary desc
limit 1 offset 1
) as SecondHighestSalary