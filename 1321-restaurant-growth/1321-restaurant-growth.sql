# Write your MySQL query statement below


SELECT
    visited_on,
    amount,
    ROUND(average_amount, 2) AS average_amount
FROM (
    SELECT
        visited_on,
        SUM(daily_amount) OVER (
            ORDER BY visited_on
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        ) AS amount,
        AVG(daily_amount) OVER (
            ORDER BY visited_on
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        ) AS average_amount,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
    FROM (
        SELECT visited_on, SUM(amount) AS daily_amount
        FROM Customer
        GROUP BY visited_on
    ) AS d
) AS result
WHERE rn >= 7
ORDER BY visited_on;
