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