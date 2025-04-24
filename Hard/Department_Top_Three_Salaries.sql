with leaderboard as (select d.name as Department, e.name as Employee, salary,
Dense_Rank() over (partition by departmentId order by salary desc) as ranks
from Department d
inner join Employee e on d.id = e.departmentId)

select Department,Employee,Salary
from leaderboard
where ranks < 4