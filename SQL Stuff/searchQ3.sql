SELECT champion.c_name, i1.i_name, i2.i_name, i3.i_name
From recommendItems, champion, items i1, items i2, items i3, (SELECT t_rank as teamRank, t_champion1 as c1, t_champion2 as c2, t_champion3 as c3, t_champion4 as c4, t_champion5 as c5, t_champion6 as c6, t_champion7 as c7, t_champion8 as c8
FROM teamComps, origin, classes  
WHERE o_name LIKE '%Prodigy%' AND
cl_name LIKE '%Cannoneer%' AND
(t_oname = o_index or t_oname2 = o_index) AND (t_clname = cl_index or t_clname2 = cl_index)
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