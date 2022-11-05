--1.)
UPDATE stats 
SET s_health_LVL_1 = 650, s_health_LVL_2 = 1700, s_health_LVL_3 = 2106 
WHERE s_name = 'Sett';

--2.) 
SELECT c_name
FROM champion
WHERE o_name = 'Lagoon';

--3.)
SELECT 