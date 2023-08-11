WITH sequence AS (
    SELECT 1 AS num
    UNION ALL
    SELECT num + 1
    FROM sequence
    WHERE num + 1 <= 1000
),
prime_numbers AS (
    SELECT B.num, SUM(CASE WHEN B.num % A.num = 0 THEN 1 ELSE 0 END) reps
    FROM sequence A
    INNER JOIN sequence B ON A.num <= B.num
    GROUP BY B.num
)
SELECT STRING_AGG(num, '&')
FROM prime_numbers
WHERE reps = 2
OPTION (maxrecursion 1000)
