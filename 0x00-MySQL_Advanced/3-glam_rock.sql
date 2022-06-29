-- This script will list band whose style is glam rock
SELECT band_name, (2022 - formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%';
