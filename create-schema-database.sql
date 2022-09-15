CREATE TABLE champion(
    c_index decimal(2,0) not null,
    c_patch_version decimal(2,2) not null, 
    c_name char(25) not null,
    c_origin1 char(15),
    c_origin2 char(15),
    c_class1 char(15) not null,
    c_class2 char(15),
    c_cost  decimal(2,0) not null,
    c_recommend_item1 varchar(25) not null,
    c_recommend_item2 varchar(25) not null,
    c_recommend_item3 varchar(25) not null,
);

CREATE TABLE stats(
    s_name char(25) not null,
    s_patch_version decimal(2,2) not null, 
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
    a_patch_version decimal(2,2) not null, 
    a_name_champion char(25) not null,
    a_name_ability char(32)
    a_ability_description varchar(500) not null,

    a_name_modifier1 varchar(25) not null,
    a_modifier1_LVL1 decimal(4,2) not null,
    a_modifier1_LVL2 decimal(4,2) not null,
    a_modifier1_LVL3 decimal(4,2) not null,

    a_name_modifier2 varchar(25),
    a_modifier2_LVL1 decimal(4,2),
    a_modifier2_LVL2 decimal(4,2),
    a_modifier2_LVL3 decimal(5,2),

    a_name_modifier3 varchar(25),
    a_modifier3_LVL1 decimal(4,2),
    a_modifier3_LVL2 decimal(4,2),
    a_modifier3_LVL3 decimal(4,2),

    a_name_modifier4 varchar(25),
    a_modifier4_LVL1 decimal(4,2),
    a_modifier4_LVL2 decimal(4,2),
    a_modifier4_LVL4 decimal(4,2),
);

CREATE TABLE origin(
    o_name char(25) not null,
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
    o_bonus_decription8 varchar(150),
);