WITH Projects_With_Days AS (
    SELECT Start_Date, End_Date,
    DATEDIFF(day, Start_Date, LAG(End_Date, 1, End_Date) OVER (ORDER BY Start_Date)) Days_Diff_Next,
    DATEDIFF(day, End_Date, LEAD(Start_Date, 1, Start_Date) OVER (ORDER BY Start_Date)) Days_Diff_Prev
    FROM Projects
),
Filtered_Projects as (
    SELECT Start_Date, 
    CASE 
        WHEN Days_Diff_Prev = 0 THEN LEAD(End_Date) OVER (ORDER BY Start_Date) 
        ELSE End_Date 
    END Real_End_Date, Days_Diff_Next
    FROM Projects_With_Days
    WHERE Days_Diff_Next != 0 
    OR Days_Diff_Prev != 0
)
SELECT Start_Date, Real_End_Date
FROM Filtered_Projects
WHERE Days_Diff_Next != 0
ORDER BY DATEDIFF(day, Start_Date, Real_End_Date), Start_Date

