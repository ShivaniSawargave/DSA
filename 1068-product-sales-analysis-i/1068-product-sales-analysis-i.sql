# Write your MySQL query statement below
select product_name, year, price
from Sales 
Join Product
on Product.product_id = Sales.product_id
