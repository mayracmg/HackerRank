SELECT H.hacker_id, H.name
FROM Submissions S
INNER JOIN Challenges C ON S.challenge_id = C.challenge_id
INNER JOIN Difficulty D ON D.difficulty_level = C.difficulty_level
    AND S.score = D.score
INNER JOIN Hackers H ON S.hacker_id = H.hacker_id
GROUP BY H.hacker_id, H.name
HAVING COUNT(S.challenge_id) > 1
ORDER BY COUNT(S.challenge_id) DESC, H.hacker_id
