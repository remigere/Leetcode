# Write your MySQL query statement below
# select gender, day, sum(score_points) over(partition by gender order by day) as score_points
# from Scores
# group by gender, day
# order by gender, day

SELECT gender, day, 
       SUM(score_points) OVER(PARTITION BY gender ORDER BY day) AS total
FROM Scores