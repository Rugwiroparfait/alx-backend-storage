-- Task: Rank country origins of bands, ordered by the number of non-unique fans
-- This script will rank the origins of bands by the total number of fans in descending order.

-- Rank country origins of bands by the number of fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

-- End of the script.
