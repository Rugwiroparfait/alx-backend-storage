-- Task: List all bands with Glam rock as their main style, ranked by their longevity.
-- This script calculates the lifespan of each band and lists those with Glam rock as their main style.

-- Select bands with Glam rock style and calculate their lifespan
SELECT 
    band_name, 
    CASE 
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM 
    metal_bands
WHERE 
    style LIKE '%Glam rock%'
ORDER BY 
    lifespan DESC;

-- End of the script.
