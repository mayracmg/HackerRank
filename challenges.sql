WITH Counts AS (
    SELECT H.Hacker_id, H.Name, COUNT(C.challenge_id) Total
    FROM Hackers H
    INNER JOIN Challenges C ON C.hacker_id = H.hacker_id
    GROUP BY H.hacker_id, H.name
),
Using_Window_Function AS (
    SELECT Hacker_id, Name, Total
    , COUNT(Hacker_id) OVER (PARTITION BY Total) AS Same_Rank
    , FIRST_VALUE(Total) OVER (ORDER BY Total DESC) AS First_Total
    FROM Counts
)
SELECT Hacker_id, Name, Total
FROM Using_Window_Function
WHERE Same_Rank = 1
OR Total = First_Total
ORDER BY total DESC, hacker_id ASC
