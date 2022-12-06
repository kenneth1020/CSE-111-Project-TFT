--1.) Update Sett's health
UPDATE stats 
SET s_health_LVL_1 = 650, s_health_LVL_2 = 1700, s_health_LVL_3 = 3000
--SET s_health_LVL_1 = 650, s_health_LVL_2 = 1700, s_health_LVL_3 = 2106  
WHERE s_index = 38;

SELECT * FROM stats 
WHERE s_index = 38;
--2.) What champions are in the Lagoon origin?
SELECT c_name
FROM champion
INNER JOIN origin ON c_origin1 = o_index
WHERE o_index = 5
Group by c_name;

--3.) From a team comp, what is the highest winrate champion. List the champion, the items.
SELECT champion.c_name, i1.i_name, i2.i_name, i3.i_name
From recommendItems, champion, items i1, items i2, items i3, (SELECT t_rank as teamRank, t_champion1 as c1, t_champion2 as c2, t_champion3 as c3, t_champion4 as c4, t_champion5 as c5, t_champion6 as c6, t_champion7 as c7, t_champion8 as c8
FROM teamComps  
WHERE (t_oname = 4 or t_oname2 =4) AND (t_clname = 12 or t_clname2 = 12)
) as t1
INNER JOIN champion ch1 ON t1.c1 = ch1.c_index
INNER JOIN champion ch2 ON t1.c2 = ch2.c_index
INNER JOIN champion ch3 ON t1.c3 = ch3.c_index
INNER JOIN champion ch4 ON t1.c4 = ch4.c_index
INNER JOIN champion ch5 ON t1.c5 = ch5.c_index
INNER JOIN champion ch6 ON (SELECT CASE WHEN t1.c6 IS NULL THEN 36
    ELSE t1.c6
    END) = ch6.c_index
INNER JOIN champion ch7 ON (SELECT CASE WHEN t1.c7 IS NULL THEN 36
    ELSE t1.c7
    END) = ch7.c_index
INNER JOIN champion ch8 ON (SELECT CASE WHEN t1.c8 IS NULL THEN 36
    ELSE t1.c8
    END) = ch8.c_index
INNER JOIN recommendItems r1 ON ch1.c_index = r1.ri_index
INNER JOIN recommendItems r2 ON ch2.c_index = r2.ri_index
INNER JOIN recommendItems r3 ON ch3.c_index = r3.ri_index
INNER JOIN recommendItems r4 ON ch4.c_index = r4.ri_index
INNER JOIN recommendItems r5 ON ch5.c_index = r5.ri_index
INNER JOIN recommendItems r6 ON ch6.c_index = r6.ri_index
INNER JOIN recommendItems r7 ON ch7.c_index = r7.ri_index
INNER JOIN recommendItems r8 ON ch8.c_index = r8.ri_index
WHERE recommendItems.ri_rank = (SELECT min(x)  
                              FROM (SELECT r1.ri_rank as x 
                                    UNION
                                    SELECT r2.ri_rank as x
                                    UNION
                                    SELECT r3.ri_rank as x
                                    UNION
                                    SELECT r4.ri_rank as x
                                    UNION
                                    SELECT r5.ri_rank as x
                                    UNION
                                    SELECT r6.ri_rank as x
                                    UNION
                                    SELECT r7.ri_rank as x
                                    UNION
                                    SELECT r8.ri_rank as x) as x)
    AND recommendItems.ri_index = champion.c_index
    AND recommendItems.ri_recommend_item1 = i1.i_index
    AND recommendItems.ri_recommend_item2 = i2.i_index
    AND recommendItems.ri_recommend_item3 = i3.i_index;

--4.)
UPDATE ability
SET a_modifier1_LVL1 = 150
-- SET a_modifier1_LVL1 = 200
WHERE a_name_ability = 'Coral Shield';

--5)
SELECT count (DISTINCT t_rank)
FROM teamComps
WHERE t_clname =12 or t_clname2 = 12;

--6)How many champion with a range more than 3. Use more than 20,000 matches
SELECT count (DISTINCT c_index)
FROM champion
INNER JOIN stats ON c_index = s_index
INNER JOIN recommendItems ON c_index = ri_index
INNER JOIN winrate ON ri_rank = w_rank
WHERE s_range > 3 AND w_num_matches_used > 20000;


--7.) Which champions have an average place lower than 4.5. List them and their classes
SELECT c_name, C1.cl_name, C2.cl_name
        FROM champion
        INNER JOIN recommendItems ON c_index = ri_index
        INNER JOIN winrate ON ri_rank = w_rank
        LEFT OUTER JOIN  classes C1 ON c_class1 = C1.cl_index
        LEFT OUTER JOIN  classes C2 ON c_class2 = C2.cl_index
        WHERE w_average_place < 4.5;

--8.) Who’s the best champion by rank in each team comps.
SELECT teamrank, champion.c_name, recommendItems.ri_rank
From recommendItems, champion, (SELECT t_rank as teamRank, t_champion1 as c1, t_champion2 as c2, t_champion3 as c3, t_champion4 as c4, t_champion5 as c5, t_champion6 as c6, t_champion7 as c7, t_champion8 as c8
FROM teamComps  
) as t1
INNER JOIN champion ch1 ON t1.c1 = ch1.c_index
INNER JOIN champion ch2 ON t1.c2 = ch2.c_index
INNER JOIN champion ch3 ON t1.c3 = ch3.c_index
INNER JOIN champion ch4 ON t1.c4 = ch4.c_index
INNER JOIN champion ch5 ON t1.c5 = ch5.c_index
INNER JOIN champion ch6 ON (SELECT CASE WHEN t1.c6 IS NULL THEN 36
    ELSE t1.c6
    END) = ch6.c_index
INNER JOIN champion ch7 ON (SELECT CASE WHEN t1.c7 IS NULL THEN 36
    ELSE t1.c7
    END) = ch7.c_index
INNER JOIN champion ch8 ON (SELECT CASE WHEN t1.c8 IS NULL THEN 36
    ELSE t1.c8
    END) = ch8.c_index
INNER JOIN recommendItems r1 ON ch1.c_index = r1.ri_index
INNER JOIN recommendItems r2 ON ch2.c_index = r2.ri_index
INNER JOIN recommendItems r3 ON ch3.c_index = r3.ri_index
INNER JOIN recommendItems r4 ON ch4.c_index = r4.ri_index
INNER JOIN recommendItems r5 ON ch5.c_index = r5.ri_index
INNER JOIN recommendItems r6 ON ch6.c_index = r6.ri_index
INNER JOIN recommendItems r7 ON ch7.c_index = r7.ri_index
INNER JOIN recommendItems r8 ON ch8.c_index = r8.ri_index
WHERE recommendItems.ri_rank = (SELECT min(x)  
                              FROM (SELECT r1.ri_rank as x 
                                    UNION
                                    SELECT r2.ri_rank as x
                                    UNION
                                    SELECT r3.ri_rank as x
                                    UNION
                                    SELECT r4.ri_rank as x
                                    UNION
                                    SELECT r5.ri_rank as x
                                    UNION
                                    SELECT r6.ri_rank as x
                                    UNION
                                    SELECT r7.ri_rank as x
                                    UNION
                                    SELECT r8.ri_rank as x) as x)
    AND recommendItems.ri_index = champion.c_index;

--9.) How many times is Sett used in each team comps
SELECT COUNT(DISTINCT t_rank)
FROM teamComps
WHERE t_champion1 = 38 
OR t_champion2 = 38
OR t_champion3 = 38
OR t_champion4 = 38
OR t_champion5 = 38
OR t_champion6 = 38
OR t_champion7 = 38 
OR t_champion8 = 38;

--10.) How expensive is each team comp cost.
SELECT teamrank, (SELECT sum(x)
              FROM (SELECT ch1.c_cost as x 
              UNION
              SELECT ch2.c_cost as x
              UNION
              SELECT ch3.c_cost as x
              UNION
              SELECT ch4.c_cost as x
              UNION
              SELECT ch5.c_cost as x
              UNION
              SELECT CASE 
              WHEN ch6.c_index = 12 THEN 0
              ELSE ch6.c_cost
              END as x
              UNION
               SELECT CASE
              WHEN ch7.c_index = 12 THEN 0
              ELSE ch7.c_cost
              END as x
              UNION
              SELECT CASE
              WHEN ch6.c_index = 12 THEN 0
              ELSE ch6.c_cost
              END as x))as costTotal
From (SELECT t_rank as teamRank, t_champion1 as c1, t_champion2 as c2, t_champion3 as c3, t_champion4 as c4, t_champion5 as c5, t_champion6 as c6, t_champion7 as c7, t_champion8 as c8
FROM teamComps  
) as t1
INNER JOIN champion ch1 ON t1.c1 = ch1.c_index
INNER JOIN champion ch2 ON t1.c2 = ch2.c_index
INNER JOIN champion ch3 ON t1.c3 = ch3.c_index
INNER JOIN champion ch4 ON t1.c4 = ch4.c_index
INNER JOIN champion ch5 ON t1.c5 = ch5.c_index
INNER JOIN champion ch6 ON (SELECT CASE WHEN t1.c6 IS NULL THEN 12
    ELSE t1.c6
    END) = ch6.c_index
INNER JOIN champion ch7 ON (SELECT CASE WHEN t1.c7 IS NULL THEN 12
    ELSE t1.c7
    END) = ch7.c_index
INNER JOIN champion ch8 ON (SELECT CASE WHEN t1.c8 IS NULL THEN 12
    ELSE t1.c8
    END) = ch8.c_index;



--11.) Insert a new team comp
INSERT INTO teamComps (t_rank, t_teir, t_oname, t_oname2, t_clname, t_clname2, t_champion1, t_champion2, t_champion3, t_champion4, t_champion5, t_champion6, t_champion7, t_champion8, t_roll_id)
VALUES(24, 'C', 5, 4, 12, 13, 24, 25, 13, 40, 61, 43, 55, 39, 1);

--12.) If Sett is in the team comp, then change the team comp tier to C
UPDATE teamComps
SET t_teir = 'B'
WHERE t_champion1 = 38
OR t_champion2 = 38 
OR t_champion3 = 38 
OR t_champion4 = 38
OR t_champion5 = 38 
OR t_champion6 = 38 
OR t_champion7 = 38 
OR t_champion8 = 38;

--13.) Which top 5 character with the highest health at level 1
SELECT c_name, s_health_LVL_1
FROM champion
INNER JOIN stats ON champion.c_index = stats.s_index
ORDER BY s_health_LVL_1 DESC
LIMIT 5;

--14.) How many components needed for this champion build
SELECT c_name, x, count(*) as numItems
FROM champion, (
        SELECT i1.i_component_1 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item1 = i1.i_index
        WHERE c_name = 'Sett'
        UNION ALL
        SELECT i1.i_component_2 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item1 = i1.i_index
        WHERE c_name = 'Sett'
        UNION ALL
        SELECT i1.i_component_1 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item2 = i1.i_index
        WHERE c_name = 'Sett'
        UNION ALL
        SELECT i1.i_component_2 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item2 = i1.i_index
        WHERE c_name = 'Sett'
        UNION ALL
        SELECT i1.i_component_1 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item3 = i1.i_index
        WHERE c_name = 'Sett'
        UNION ALL
        SELECT i1.i_component_2 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item3 = i1.i_index
        WHERE c_name = 'Sett')
WHERE c_name = 'Sett'
GROUP BY x
Order BY numItems DESC;

--15.) Which are the top 5 champion has the highest attack speed 
SELECT c_name, s_attack_speed
FROM champion
INNER JOIN stats ON champion.c_index = stats.s_index
ORDER BY s_attack_speed DESC
LIMIT 5;

--16.) What does B.F. Sword build into. List the item and their components
SELECT i_name, i_component_1, i_component_2
FROM items
WHERE i_component_1 = 'B.F. Sword' OR i_component_2 = 'B.F. Sword';

--17.) What does all items that use Spatula gives you
SELECT i_name, i_description
FROM items
WHERE i_component_1 LIKE '%Spatula%' or 
i_component_2 LIKE '%Spatula%';

--18.) Count the roll types of all comps that have the Jade Origin
SELECT DISTINCT t_rank, t_oname, t_oname2, t_clname, t_clname2, r_type
FROM rollType
INNER JOIN teamComps ON r_index = t_roll_id
WHERE t_oname = 4 OR t_oname2 = 4;


--19.) LIST the S rank items
SELECT i_name, i_description
FROM items
WHERE i_tier = 'S';

--20.) How many components needed are for need for all champions from winrate.
SELECT x, count(x)
FROM (SELECT i1.i_component_1 as x
    FROM winrate
    INNER JOIN items i1 ON w_top_item1 = i1.i_index
    UNION ALL
    SELECT i1.i_component_2 as x
    FROM winrate
    INNER JOIN items i1 ON w_top_item1 = i1.i_index
    UNION ALL
    SELECT i2.i_component_1 as x
    FROM winrate
    INNER JOIN items i2 ON w_top_item2 = i2.i_index
    UNION ALL
    SELECT i2.i_component_2 as x
    FROM winrate
    INNER JOIN items i2 ON w_top_item2 = i2.i_name
    UNION ALL
    SELECT i3.i_component_1 as x
    FROM winrate
    INNER JOIN items i3 ON w_top_item3 = i3.i_index
    UNION ALL
    SELECT i3.i_component_2 as x
    FROM winrate
    INNER JOIN items i3 ON w_top_item3 = i3.i_index
    UNION ALL
    SELECT i4.i_component_1 as x
    FROM winrate
    INNER JOIN items i4 ON w_top_item4 = i4.i_index
    UNION ALL
    SELECT i4.i_component_2 as x
    FROM winrate
    INNER JOIN items i4 ON w_top_item4 = i4.i_index)
GROUP BY x
ORDER BY count(x);

--21.) LIST all ability that has damage
SELECT DISTINCT a_index, a_name_ability
FROM ability
WHERE a_name_modifier1 LIKE '%damage%' 
or a_name_modifier2 LIKE '%damage%'
or a_name_modifier3 LIKE '%damage%'
or a_name_modifier4 LIKE '%damage%';

