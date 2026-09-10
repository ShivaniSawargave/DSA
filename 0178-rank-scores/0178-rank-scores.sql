# Write your MySQL query statement below
Select
score,  Dense_rank() Over ( Order by score DESC) as 'rank'
From Scores