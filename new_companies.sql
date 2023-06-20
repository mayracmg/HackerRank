SELECT C.company_code, C.founder
, COUNT(DISTINCT L.lead_manager_code)
, COUNT(DISTINCT S.senior_manager_code)
, COUNT(DISTINCT M.manager_code)
, COUNT(DISTINCT E.employee_code)
FROM Company C
INNER JOIN Lead_Manager L ON C.company_code = L.company_code
INNER JOIN Senior_Manager S ON S.company_code = C.company_code
    AND L.lead_manager_code = S.lead_manager_code
INNER JOIN Manager M ON M.company_code = C.company_code
    AND L.lead_manager_code = M.lead_manager_code
    AND S.senior_manager_code = M.senior_manager_code
INNER JOIN Employee E ON E.company_code = C.company_code
    AND L.lead_manager_code = E.lead_manager_code
    AND S.senior_manager_code = E.senior_manager_code
    AND M.manager_code = E.manager_code
GROUP BY C.company_code, C.founder
ORDER BY C.company_code
