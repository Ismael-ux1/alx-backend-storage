-- This script ranks country origins of bands, ordered by the number of (non-unique) fans.

-- This script can be executed on any database.

--  Select the 'origin' and count the number of 'fans' for each 'origin'
SELECT origin, COUNT(fans) AS nb_fans

-- From the 'metal_bands' table
FROM metal_bands

-- Group the result by 'origin'
GROUP BY origin

-- Order the groups by the number of fans in descending order
ORDER BY nb_fans DESC;
