-- a script that lists all records of the table second_table
-- Don’t list rows without a name value
SELECT score, name FROM hbtn_0c_0 WHERE name IS NOT NULL
