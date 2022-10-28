/* The Manhattan Distance is |x1 - x2| + |y1 - y2| = |a - c| + |b - d| 
or (d-b) + (c-a) */
SELECT ROUND(ABS(MIN(LAT_N)-MAX(LAT_N)) + ABS(MIN(LONG_W)-MAX(LONG_W)), 4) 
FROM STATION