# Write your MySQL query statement below
(
    SELECT U.name AS results
    FROM Users U
    JOIN MovieRating M
    ON U.user_id = M.user_id
    GROUP BY U.user_id, U.name
    ORDER BY COUNT(*) DESC, U.name ASC
    LIMIT 1
)

UNION ALL

(
    SELECT Mo.title AS results
    FROM Movies Mo
    JOIN MovieRating M
    ON Mo.movie_id = M.movie_id
    WHERE M.created_at >= '2020-02-01'
      AND M.created_at < '2020-03-01'
    GROUP BY Mo.movie_id, Mo.title
    ORDER BY AVG(M.rating) DESC, Mo.title ASC
    LIMIT 1
);