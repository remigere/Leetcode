# Write your MySQL query statement below


# select e.employee_id, (select count(team_id) from Employee where team_id = e.team_id) as team_size
# from Employee as e

# SELECT employee_id, 
#     COUNT(team_id) OVER(PARTITION BY team_id) AS team_size
# FROM Employee

# select employee_id, count(*) over(partition by team_id) as team_size
# from employee

SELECT e.employee_id, team_size
FROM Employee AS e
LEFT JOIN (
      SELECT team_id, COUNT(employee_id) AS team_size
      FROM Employee
      GROUP BY team_id
) AS teams
ON e.team_id = teams.team_id