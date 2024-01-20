-- Select the 'band_name' and compute the lifespan for each band with 'Glam rock',
-- ranked by their longevity

-- Select band_name and compute lifespan using formed and split attributes
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC
