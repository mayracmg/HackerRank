WITH Max_scores AS (
    SELECT hacker_id, challenge_id, MAX(score) score
    FROM Submissions
    GROUP BY challenge_id, hacker_id
),
Summary AS (
    SELECT H.hacker_id, H.name, SUM(score) score
    FROM Hackers H
    INNER JOIN Max_scores M ON M.hacker_id = H.hacker_id
    GROUP BY H.hacker_id, H.name
)
SELECT hacker_id, name, score
FROM Summary H
WHERE score > 0
ORDER BY score DESC, hacker_id
