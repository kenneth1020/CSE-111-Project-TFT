--delete from champion;
--delete from stats;

--DROP TABLE Champion;
DROP Table rollType;
DROP TABLE teamComps;
CREATE TABLE rollType(
    r_id decimal(2,0) not null,
    r_type varchar(25) not null,
    r_description varchar(300) not null
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