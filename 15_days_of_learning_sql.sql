WITH Hacker_Submissions AS (
    SELECT submission_date, hacker_id, COUNT(submission_id) total_submissions, 
	RANK() OVER(PARTITION BY hacker_id ORDER BY submission_date) consecutive_days
    FROM Submissions
    GROUP BY submission_date, hacker_id
),
Count_Hackers AS (
    SELECT submission_date, COUNT(hacker_id) total_hackers
    FROM Hacker_Submissions 
    WHERE consecutive_days = DAY(submission_date)
    GROUP BY submission_date
),
Total_Submissions AS (
    SELECT S.submission_date, C.total_hackers, S.hacker_id, FIRST_VALUE(S.hacker_id) OVER(PARTITION BY S.submission_date ORDER BY total_submissions DESC, hacker_id) best_hacker_id
    FROM Hacker_Submissions S
    INNER JOIN Count_Hackers C ON S.submission_date = C.submission_date
)
SELECT submission_date, total_hackers, H.hacker_id, H.name
FROM Total_Submissions T
INNER JOIN hackers H ON H.hacker_id = T.hacker_id
WHERE H.hacker_id = T.best_hacker_id
ORDER BY submission_date 
