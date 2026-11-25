# Write your MySQL query statement below
select P.product_name, sum(O.unit) as unit
from Products P
join Orders O
on P.product_id = O.product_id
where Year(order_date) = 2020 and month(order_date) = 02
group by P.product_name 
having sum(O.unit) >=100