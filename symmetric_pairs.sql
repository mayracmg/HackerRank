WITH Data_With_ID AS (
    SELECT X, Y, 
    ROW_NUMBER() OVER(ORDER BY X, Y ASC) AS ID
    FROM Functions
)
SELECT DISTINCT F1.X, F1.Y
FROM Data_With_ID F1
INNER JOIN Data_With_ID F2 ON F1.X = F2.Y AND F2.X = F1.Y
WHERE F1.X <= F1.Y
AND F1.ID != F2.ID
ORDER BY F1.X, F1.Y
