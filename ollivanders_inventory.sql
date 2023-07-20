--Opcion1
SELECT W.id, P.age, W.coins_needed, W.power
FROM Wands W
INNER JOIN Wands_Property P ON P.code = W.code
WHERE P.is_evil = 0
AND W.coins_needed = (
    SELECT MIN(coins_needed)
    FROM Wands Y
    WHERE Y.code = W.code
    AND Y.power = W.power
)
ORDER BY W.power DESC, P.age DESC

--Opcion 2
WITH All_Wands AS (
	SELECT W.id, P.age, W.coins_needed, W.power,
    ROW_NUMBER() OVER(PARTITION BY W.code, W.power ORDER BY W.coins_needed) rownum
    FROM Wands W
    INNER JOIN Wands_Property P ON P.code = W.code
    WHERE P.is_evil = 0
)
SELECT id, age, coins_needed, power
FROM All_Wands
WHERE rownum = 1
ORDER BY power DESC, age DESC
