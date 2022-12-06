import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)
    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    return conn


def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)
    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def dropTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")
    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE champion;"
        _conn.execute(sql)
        sql = "DROP TABLE stats;"
        _conn.execute(sql)
        sql = "DROP TABLE ability;"
        _conn.execute(sql)
        sql = "DROP TABLE origin;"
        _conn.execute(sql)
        sql = "DROP TABLE classes;"
        _conn.execute(sql)
        sql = "DROP TABLE items;"
        _conn.execute(sql)
        sql = "DROP TABLE winrate;"
        _conn.execute(sql)
        sql = "DROP TABLE recommendedItems;"
        _conn.execute(sql)
        sql = "DROP TABLE teamsComps;"
        _conn.execute(sql)
        sql = "DROP TABLE rollType;"
        _conn.execute(sql)
        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def createTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create tables")
    _conn.execute("BEGIN")
    try:
        sql = """CREATE TABLE champion(
        c_index decimal(2,0) not null,
        c_name char(25) not null,
        c_tier char(1) not null,
        c_origin1 char(15),
        c_origin2 char(15),
        c_class1 char(15) not null,
        c_class2 char(15),
        c_cost decimal(2,0) not null)"""
        _conn.execute(sql)

        sql = """CREATE TABLE ability(
        a_index decimal(2,0) not null,
        a_name varchar(25) not null,
        a_tier char(1) not null,
        a_description varchar(300) not null,
        a_name_modifier1 varchar(35),
        a_modifier1_LVL1 decimal(4,2),
        a_modifier1_LVL2 decimal(4,2),
        a_modifier1_LVL3 decimal(4,2),
        a_name_modifier2 varchar(35),
        a_modifier2_LVL1 decimal(4,2),
        a_modifier2_LVL2 decimal(4,2),
        a_modifier2_LVL3 decimal(5,2),
        a_name_modifier3 varchar(35),
        a_modifier3_LVL1 decimal(4,2),
        a_modifier3_LVL2 decimal(4,2),
        a_modifier3_LVL3 decimal(4,2),
        a_name_modifier4 varchar(35),
        a_modifier4_LVL1 decimal(4,2),
        a_modifier4_LVL2 decimal(4,2),
        a_modifier4_LVL4 decimal(4,2)
        )
        """
        _conn.execute(sql)

        sql = """CREATE TABLE origin(
        o_name varchar(25) not null,
        o_tier char(1) not null,
        o_description varchar(300) not null,
        o_requirement1 decimal(1,0) not null,
        o_bonus_decription1 varchar(150) not null,
        o_requirement2 decimal(1,0) not null,
        o_bonus_decription2 varchar(150) not null,
        o_requirement3 decimal(1,0) not null,
        o_bonus_decription3 varchar(150) not null,
        o_requirement4 decimal(2,0),
        o_bonus_decription4 varchar(150),
        o_requirement5 decimal(2,0),
        o_bonus_decription5 varchar(150),
        o_requirement6 decimal(2,0),
        o_bonus_decription6 varchar(150),
        o_requirement7 decimal(2,0),
        o_bonus_decription7 varchar(150),
        o_requirement8 decimal(2,0),
        o_bonus_decription8 varchar(150)
        )
        """
        _conn.execute(sql)

        sql = """CREATE TABLE rollType(
        r_id decimal(2,0) not null,
        r_type varchar(25) not null,
        r_description varchar(300) not null
        )"""

        _conn.execute(sql)

        sql = """CREATE TABLE recommendItems(
        ri_index decimal(2,0) not null,
        ri_recommend_item1 varchar(25) not null,
        ri_recommend_item2 varchar(25) not null,
        ri_recommend_item3 varchar(25) not null,
        ri_rank decimal(2,0)
        )"""
        _conn.execute(sql)

        sql = """CREATE TABLE stats(
        s_index decimal(2,0) not null,
        s_name varchar(25) not null, 
        s_health_LVL_1 decimal(4,0) not null,
        s_health_LVL_2 decimal(4,0) not null,
        s_health_LVL_3 decimal(4,0) not null,
        s_mana decimal(3,0) not null,
        s_starting_mana decimal(3,0) not null,
        s_armor decimal(3,0) not null,
        s_magic_resistance decimal(3,0) not null,
        s_damage_per_second_LVL_1 decimal(3,0) not null,
        s_damage_per_second_LVL_2 decimal(3,0) not null,
        s_damage_per_second_LVL_3 decimal(3,0) not null,
        s_damage_LVL_1 decimal(3,0) not null,
        s_damage_LVL_2 decimal(3,0) not null,
        s_damage_LVL_3 decimal(3,0) not null,
        s_attack_speed decimal(1,2) not null,
        s_critical_rate decimal(3,0) not null,
        s_range decimal(1,0) not null
        )"""
        _conn.execute(sql)

        sql = """CREATE TABLE classes(
        cl_name varchar(25) not null,
        cl_tier char(1) not null,
        cl_description varchar(300) not null,
        cl_requirement1 decimal(1,0) not null,
        cl_bonus_decription1 varchar(150) not null,
        cl_requirement2 decimal(1,0) not null,
        cl_bonus_decription2 varchar(150) not null,
        cl_requirement3 decimal(1,0) not null,
        cl_bonus_decription3 varchar(150) not null,
        cl_requirement4 decimal(2,0),
        cl_bonus_decription4 varchar(150),
        cl_requirement5 decimal(2,0),
        cl_bonus_decription5 varchar(150)
        )"""
        _conn.execute(sql)
        sql = """CREATE TABLE items(
        i_name varchar(25) not null,
        i_description var(300) not null,
        i_tier char(1) not null,
        i_component_1 char(30) not null,
        i_component_2 char(30) not null,
        i_stat_boost1 char(30) not null,
        i_stat_number1 decimal(2,0) not null,
        i_stat_boost2 char(30),
        i_stat_number2 decimal(2,0)
        )"""
        _conn.execute(sql)

        sql = """CREATE TABLE winrate(
        w_rank decimal(2,0) not null,
        w_win_rate decimal(2,1) not null,
        w_average_place decimal(1,1) not null,
        w_top_4_rate decimal(2,1) not null,
        w_top_item1 varchar(27) not null,
        w_top_item2 varchar(27) not null,
        w_top_item3 varchar(27) not null,
        w_top_item4 varchar(27) not null,
        w_num_matches_used decimal(6,0) not null
        )"""
        _conn.execute(sql)

        sql="""CREATE TABLE teamComps(
        t_rank decimal(2,0) not null,
        t_teir char(1) not null,
        t_oname varchar(25),
        t_oname2 varchar(25),
        t_clname varchar(25) not null,
        t_clname2 varchar(25),
        t_champion1 varchar(25) not null,
        t_champion2 varchar(25) not null,
        t_champion3 varchar(25) not null,
        t_champion4 varchar(25) not null,
        t_champion5 varchar(25) not null,
        t_champion6 varchar(25),
        t_champion7 varchar(25),
        t_champion8 varchar(25),
        t_roll_id decimal(2,0) not null
        )"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def populateTables_rollType(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populating Roll Type")
    try:
        roll = [(1, "Standard", "Flexible strategy focused around a healthy economy while still keeping up in levels. General rules are Level 6 by 3-2, Level 7 by 4-1, and Level 8 by 5-1."),
            (2, "Hyper Roll", "Save up and then 3-star units at 3-1 by rolling all your gold"),
            (3,"Slow Roll (6)","3-star units at level 6 by rolling all your gold every round."),
            (4,"Slow Roll (7)","3-star units at level 7 by rolling all your gold every round."),
            (5,"Fast 8", "The goal is to reach level 8 early in Stage 4 to find 4 and 5 cost units before your oppoonents. You genreally need long win or losestreaks to have enough gold for it.")
        ]

        sql ="INSERT INTO rollType VALUES(?,?,?)"
        _conn.executemany(sql, roll)
        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def championSearch(_conn, _champion):
    print("++++++++++++++++++++++++++++++++++")
    print("Searching for champion")
    try:
        sql = """SELECT c_name, x, count(*) as numItems 
        FROM champion, (
        SELECT i1.i_component_1 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item1 = i1.i_index
        WHERE c_name = ?
        UNION ALL
        SELECT i1.i_component_2 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item1 = i1.i_index
        WHERE c_name = ?
        UNION ALL
        SELECT i1.i_component_1 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item2 = i1.i_index
        WHERE c_name = ?
        UNION ALL
        SELECT i1.i_component_2 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item2 = i1.i_index
        WHERE c_name = ?
        UNION ALL
        SELECT i1.i_component_1 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item3 = i1.i_index
        WHERE c_name = ?
        UNION ALL
        SELECT i1.i_component_2 as x
        FROM champion
            INNER JOIN recommendItems ON c_index = ri_index
            INNER JOIN items i1 ON ri_recommend_item3 = i1.i_index
        WHERE c_name = ?)
        WHERE c_name = ?
        GROUP BY x
        Order BY numItems DESC;"""
        args = [_champion, _champion, _champion, _champion, _champion, _champion, _champion]
        cur = _conn.cursor()
        cur.execute(sql, args)
        l = '{:>10} {:>20} {:>10}'.format("Champion", "Item", "Count")
        print(l)
        print("--------------------------------------------------")

        rows=cur.fetchall()
        for row in rows:
            l = '{:>10} {:>20} {:>10}'.format(row[0], row[1], row[2])
            print(l)

        return rows

    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def championData(_conn):
    try:
        sql="""SELECT c_name, 
(CASE WHEN o1.o_name IS NULL THEN "None" 
ELSE o1.o_name END) as Origin1,
(CASE WHEN o2.o_name IS NULL THEN "None" 
ELSE o2.o_name END) as Origin2, 
(CASE WHEN c1.cl_name IS NULL THEN "None" 
ELSE c1.cl_name END) as Class1,
(CASE WHEN c2.cl_name IS NULL THEN "None" 
ELSE c2.cl_name END) as Class2, c_cost
FROM Champion
LEFT OUTER JOIN origin o1 ON o1.o_index = c_origin1 
LEFT OUTER JOIN origin o2 ON o2.o_index = c_origin2
LEFT OUTER JOIN classes c1 ON c1.cl_index = c_class1
LEFT OUTER JOIN classes c2 ON c2.cl_index = c_class2;"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10} {:>20} {:>20} {:>20} {:>20} {:>10}'.format("Champion", "Origin1", "Origin2", "Class1", "Class2", "Cost")
        print(l)
        print("--------------------------------------------------")

        rows=cur.fetchall()
        for row in rows:
            l = '{:>10} {:>20} {:>20} {:>20} {:>20} {:>10}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
            print(l)

        return rows

    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def championPlacement(_conn, _num):
    print("++++++++++++++++++++++++++++++++++")
    print("Searching for Champion Placement")
    try:
        sql = """SELECT c_name, C1.cl_name, (CASE WHEN C2.cl_name IS NULL THEN "NONE" ELSE C2.cl_name END) as Class2
        FROM champion
        INNER JOIN recommendItems ON c_index = ri_index
        INNER JOIN winrate ON ri_rank = w_rank
        LEFT OUTER JOIN  classes C1 ON c_class1 = C1.cl_index
        LEFT OUTER JOIN  classes C2 ON c_class2 = C2.cl_index
        WHERE w_average_place < ? ;"""
        args = [_num]
        cur = _conn.cursor()
        cur.execute(sql, args)
        l = '{:>20} {:>20} {:>20}'.format("Champion","Class1","Class2")
        print(l)
        print("--------------------------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>20} {:>20} {:>20}'.format(row[0], row[1], row[2])
            print(l)
        
        return rows

    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def compTopChampions(_conn, _origin, _class):
    try: 
        sql = """SELECT champion.c_name, i1.i_name, i2.i_name, i3.i_name
From recommendItems, champion, items i1, items i2, items i3, (SELECT t_rank as teamRank, t_champion1 as c1, t_champion2 as c2, t_champion3 as c3, t_champion4 as c4, t_champion5 as c5, t_champion6 as c6, t_champion7 as c7, t_champion8 as c8
FROM teamComps, origin, classes  
WHERE o_name LIKE ? AND
cl_name LIKE ? AND
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
    AND recommendItems.ri_recommend_item3 = i3.i_index; """
        args = [_origin, _class]
        cur = _conn.cursor()
        cur.execute(sql, args)
        l = '{:>10} {:>20}'.format("Champion", "Item 1", "Item 2", "Item 3")
        print(l)
        print("--------------------------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>20}'.format(row[0], row[1])
            print(l)

        return rows

    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def originData(_conn):
    try:
        sql="""Select o_index, o_name, o_tier, o_description, o_requirement1, o_bonus_decription1,
        (CASE WHEN o_requirement2 IS NULL THEN "None" ELSE o_requirement2 END),
        (CASE WHEN o_bonus_decription2 IS NULL THEN "None" ELSE o_bonus_decription2 END),
        (CASE WHEN o_requirement3 IS NULL THEN "None" ELSE o_requirement3 END),
        (CASE WHEN o_bonus_decription3 IS NULL THEN "None" ELSE o_bonus_decription3 END),
        (CASE WHEN o_requirement4 IS NULL THEN "None" ELSE o_requirement4 END),
        (CASE WHEN o_bonus_decription4 IS NULL THEN "None" ELSE o_bonus_decription4 END),
        (CASE WHEN o_requirement5 IS NULL THEN "None" ELSE o_requirement5 END),
        (CASE WHEN o_bonus_decription5 IS NULL THEN "None" ELSE o_bonus_decription5 END),
        (CASE WHEN o_requirement6 IS NULL THEN "None" ELSE o_requirement6 END),
        (CASE WHEN o_bonus_decription6 IS NULL THEN "None" ELSE o_bonus_decription6 END),
        (CASE WHEN o_requirement7 IS NULL THEN "None" ELSE o_requirement7 END),
        (CASE WHEN o_bonus_decription7 IS NULL THEN "None" ELSE o_bonus_decription7 END),
        (CASE WHEN o_requirement8 IS NULL THEN "None" ELSE o_requirement8 END),
        (CASE WHEN o_bonus_decription8 IS NULL THEN "None" ELSE o_bonus_decription8 END)
        FROM origin;"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10}'.format("Index","Origin","Tier","Description","Required1","Bonus1", "Required2","Bonus2", "Required3","Bonus3", "Required4","Bonus4", "Required5","Bonus5", "Required6","Bonus6", "Required7","Bonus7", "Required8","Bonus8")
        print(l)
        print("--------------------------------------------------")

        rows=cur.fetchall()
        for row in rows:
            l = '{:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])
            print(l)

        return rows

    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def originSearch(_conn, _origin):
    try:
        sql="""Select o_index, o_name, o_tier, o_description, o_requirement1, o_bonus_decription1,
        (CASE WHEN o_requirement2 IS NULL THEN "None" ELSE o_requirement2 END),
        (CASE WHEN o_bonus_decription2 IS NULL THEN "None" ELSE o_bonus_decription2 END),
        (CASE WHEN o_requirement3 IS NULL THEN "None" ELSE o_requirement3 END),
        (CASE WHEN o_bonus_decription3 IS NULL THEN "None" ELSE o_bonus_decription3 END),
        (CASE WHEN o_requirement4 IS NULL THEN "None" ELSE o_requirement4 END),
        (CASE WHEN o_bonus_decription4 IS NULL THEN "None" ELSE o_bonus_decription4 END),
        (CASE WHEN o_requirement5 IS NULL THEN "None" ELSE o_requirement5 END),
        (CASE WHEN o_bonus_decription5 IS NULL THEN "None" ELSE o_bonus_decription5 END),
        (CASE WHEN o_requirement6 IS NULL THEN "None" ELSE o_requirement6 END),
        (CASE WHEN o_bonus_decription6 IS NULL THEN "None" ELSE o_bonus_decription6 END),
        (CASE WHEN o_requirement7 IS NULL THEN "None" ELSE o_requirement7 END),
        (CASE WHEN o_bonus_decription7 IS NULL THEN "None" ELSE o_bonus_decription7 END),
        (CASE WHEN o_requirement8 IS NULL THEN "None" ELSE o_requirement8 END),
        (CASE WHEN o_bonus_decription8 IS NULL THEN "None" ELSE o_bonus_decription8 END)
        FROM origin
        WHERE o_name = ?;"""
        args = [_origin]    
        cur = _conn.cursor()
        cur.execute(sql,args)
        l = '{:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10}'.format("Index","Origin","Tier","Description","Required1","Bonus1", "Required2","Bonus2", "Required3","Bonus3", "Required4","Bonus4", "Required5","Bonus5", "Required6","Bonus6", "Required7","Bonus7", "Required8","Bonus8")
        print(l)
        print("--------------------------------------------------")

        rows=cur.fetchall()
        for row in rows:
            l = '{:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10} {:>5} {:>10}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])
            print(l)

        return rows

    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def championInfo(_conn, _champion):
    try:
        sql="""SELECT c_name, 
(CASE WHEN o1.o_name IS NULL THEN "None" 
ELSE o1.o_name END) as Origin1,
(CASE WHEN o2.o_name IS NULL THEN "None" 
ELSE o2.o_name END) as Origin2, 
(CASE WHEN c1.cl_name IS NULL THEN "None" 
ELSE c1.cl_name END) as Class1,
(CASE WHEN c2.cl_name IS NULL THEN "None" 
ELSE c2.cl_name END) as Class2, c_cost,
s_mana,
s_starting_mana,
s_armor,
s_magic_resistance,
s_attack_speed,
s_critical_rate,
s_range,
a_name_ability,
a_ability_description
FROM Champion
LEFT OUTER JOIN origin o1 ON o1.o_index = c_origin1 
LEFT OUTER JOIN origin o2 ON o2.o_index = c_origin2
LEFT OUTER JOIN classes c1 ON c1.cl_index = c_class1
LEFT OUTER JOIN classes c2 ON c2.cl_index = c_class2
INNER JOIN stats ON c_stats = s_index
INNER JOIN ability on c_ability = a_index
WHERE c_name = ?;"""
        args = [_champion]
        cur = _conn.cursor()
        cur.execute(sql, args)
        l = '{:>10} {:>15} {:>15} {:>15} {:>15} {:>10} {:>10} {:>10} {:>10} {:>20} {:>20} {:>10} {:>10} {:>20} {:>30}'.format("Champion", "Origin1", "Origin2", "Class1", "Class2", "Cost", "Mana", "Starting Mana", "Armor", "Magic Resistance", "Attack Speed", "Critical Rate", "Range", "Ability", "Ability Description")
        print(l)
        print("--------------------------------------------------")

        rows=cur.fetchall()
        for row in rows:
            l = '{:>10} {:>15} {:>15} {:>15} {:>15} {:>10} {:>10} {:>10} {:>10} {:>20} {:>20} {:>10} {:>10} {:>20} {:>30}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])
            print(l)

        return rows

    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

    
def main():
    database = r"tft_data.sqlite"
    # create a database connection
    conn = openConnection(database)
    with conn:
        #dropTables(conn)
        #createTables(conn)
        #populateTables_rollType(conn)
        #championSearch(conn, "Sett")
        #championData(conn)
        #championPlacement(conn, 4.5) 
        originData(conn)
    closeConnection(conn, database)
if __name__ == '__main__':
    main()
#python3 SQLite.py