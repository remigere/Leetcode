# Write your MySQL query statement below
select player_id, player_name, grand_slams_count from
(select player_id, player_name, 
(select sum(Wimbledon = player_id) + sum(Fr_open = player_id) + sum(US_open = player_id) + sum(Au_open = player_id) from Championships) as grand_slams_count
from players) as sub
where grand_slams_count > 0