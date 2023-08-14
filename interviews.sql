WITH Stats AS (
    SELECT challenge_id, 
    0 total_submissions, 0 total_accepted_submissions,
    total_views, total_unique_views
    FROM View_Stats
    
    UNION ALL
    
    SELECT challenge_id, 
    total_submissions, total_accepted_submissions,
    0 total_views, 0 total_unique_views
    FROM Submission_Stats
),
Totals AS (
    SELECT challenge_id, 
    SUM(total_submissions) total_submissions, 
    SUM(total_accepted_submissions) total_accepted_submissions,
    SUM(total_views) total_views,
    SUM(total_unique_views) total_unique_views
    FROM Stats
    GROUP BY challenge_id
)
SELECT C.contest_id, C.hacker_id, C.name,
SUM(T.total_submissions), SUM(T.total_accepted_submissions),
SUM(T.total_views), SUM(T.total_unique_views )
FROM Contests C
INNER JOIN Colleges U ON C.contest_id = U.contest_id
INNER JOIN Challenges R ON R.college_id = U.college_id
LEFT JOIN Totals T ON T.challenge_id = R.challenge_id
GROUP BY C.contest_id, C.hacker_id, C.name
