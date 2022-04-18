# Write your MySQL query statement below
select country_name, 
case when avg(weather_state) <= 15 then "Cold"
    when avg(weather_state) >= 25 then "Hot"
    else "Warm"
    end as weather_type
from countries natural join weather
where MONTH(day) = "11"
group by country_id