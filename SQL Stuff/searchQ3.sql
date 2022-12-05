SELECT c_name, 
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
LEFT OUTER JOIN classes c2 ON c2.cl_index = c_class2;