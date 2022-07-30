# Write your MySQL query statement below
# select u.user1_id, u.user2_id, u2.user1_id, u1.user2_id
# from friendship u
# join friendship u2
# on u.user2_id = u2.user2_id and u.user1_id != u2.user1_id
# join friendship u1
# on u.user1_id = u1.user1_id and u.user2_id != u1.user2_id
# group by 1, 2




with f as (
select user1_id, user2_id 
from Friendship
union 
select user2_id user1_id, user1_id user2_id
from Friendship
)

select u.user1_id, u.user2_id, count(u2.user2_id) common_friend
from friendship u
join f u1
on u.user1_id = u1.user1_id
join f u2
on u.user2_id = u2.user1_id
and u1.user2_id = u2.user2_id
group by u.user1_id, u.user2_id
having count(u2.user2_id) >= 3

# select a.user1_id, a.user2_id, count(c.user2_id) common_friend
# from Friendship a 
# join f b 
# on a.user1_id = b.user1_id # u1 friends
# join f c 
# on a.user2_id = c.user1_id # u2 friends
# and b.user2_id = c.user2_id # u1 u2 comman friends
# group by a.user1_id, a.user2_id
# having count(c.user2_id) >= 3