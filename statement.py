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


def main():
    database = r"tft_data.sqlite"
    # create a database connection
    conn = openConnection(database)
    with conn:
        #dropTables(conn)
        #createTables(conn)
        #populateTables_rollType(conn)
        championSearch(conn, "Sett")
        #championData(conn)
    
    closeConnection(conn, database)
if __name__ == '__main__':
    main()
#python3 SQLite.py