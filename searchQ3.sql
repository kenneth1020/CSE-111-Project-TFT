--3.)

SELECT CASE WHEN t1.c8 LIKE "%NULL%" THEN 'Senna'
    ELSE t1.c8
    END
From (SELECT t_rank as teamRank, t_champion1 as c1, t_champion2 as c2, t_champion3 as c3, t_champion4 as c4, t_champion5 as c5, t_champion6 as c6, t_champion7 as c7, t_champion8 as c8
                FROM teamComps  
                WHERE t_oname = 'Jade' AND t_clname = 'Shapeshifter'
                ) as t1;    