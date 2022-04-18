# Write your MySQL query statement below
select left_operand, operator, right_operand,
case when operator = ">" then if((select value from variables where name = left_operand) > (select value from variables where name = right_operand), "true", "false")
    when operator = "<" then if((select value from variables where name = left_operand) < (select value from variables where name = right_operand), "true", "false")
    else if((select value from variables where name = left_operand) = (select value from variables where name = right_operand), "true", "false") END as value

from expressions