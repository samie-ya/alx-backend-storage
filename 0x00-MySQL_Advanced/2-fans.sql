-- This script will get the highest number of fans from a band and it's country
SELECT origin, MAX(fans) AS nb_fans
	FROM metal_bands
	GROUP BY origin; 
