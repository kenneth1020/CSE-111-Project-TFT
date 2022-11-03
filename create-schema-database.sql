--Clearing table for new dataset
/*
DROP TABLE champion;
DROP TABLE stats;
DROP TABLE ability;
DROP TABLE origin;
DROP TABLE classes;
DROP TABLE items;
DROP TABLE winrate;
DROP TABLE recommendedItems;
DROP TABLE teamsComps;
DROP TABLE rollType;
*/
--Creating tables for dataset
CREATE TABLE champion(
    c_index decimal(2,0) not null,
    c_name char(25) not null,
    c_tier char(1) not null,
    c_origin1 char(15),
    c_origin2 char(15),
    c_class1 char(15) not null,
    c_class2 char(15),
    c_cost  decimal(2,0) not null
);

CREATE TABLE recommendItems(
    ri_index decimal(2,0) not null,
    ri_recommend_item1 varchar(25) not null,
    ri_recommend_item2 varchar(25) not null,
    ri_recommend_item3 varchar(25) not null,
    ri_rank decimal(2,0)
);

CREATE TABLE stats(
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
);

CREATE TABLE ability(
    a_key decimal(2,0),
    a_name_ability char(32),
    
    a_ability_description varchar(500) not null,

    a_name_modifier1 varchar(35) not null,
    a_modifier1_LVL1 decimal(4,2) not null,
    a_modifier1_LVL2 decimal(4,2) not null,
    a_modifier1_LVL3 decimal(4,2) not null,

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
);

CREATE TABLE origin(
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
);

CREATE TABLE classes(
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
);

CREATE TABLE items(
    i_name varchar(25) not null,
    i_description var(300) not null,
    i_tier char(1) not null,
    i_component_1 char(30) not null,
    i_component_2 char(30) not null,
    i_stat_boost1 char(30) not null,
    i_stat_number1 decimal(2,0) not null,
    i_stat_boost2 char(30),
    i_stat_number2 decimal(2,0)
);

CREATE TABLE winrate(
    w_rank decimal(2,0) not null,
    w_win_rate decimal(2,1) not null,
    w_average_place decimal(1,1) not null,
    w_top_4_rate decimal(2,1) not null,
    w_top_item1 varchar(27) not null,
    w_top_item2 varchar(27) not null,
    w_top_item3 varchar(27) not null,
    w_top_item4 varchar(27) not null,
    w_num_matches_used decimal(6,0) not null
);

CREATE TABLE teamComps(
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
);

CREATE TABLE rollType(
    r_id decimal(2,0) not null,
    r_type varchar(25) not null,
    r_description varchar(300) not null
);