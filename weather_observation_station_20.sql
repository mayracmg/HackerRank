WITH CTE AS (
    SELECT lat_n, ROW_NUMBER() OVER(ORDER BY lat_n ASC) rownum,
    (SELECT COUNT(id) from station) / 2.0 middle
    FROM station
)
SELECT CAST(AVG(lat_n) AS DECIMAL(10, 4))
FROM CTE
WHERE CTE.rownum >= ROUND(middle, 0)
AND CTE.rownum <= FLOOR(middle) + 1
