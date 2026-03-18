SELECT COUNT(shot_id) as count_shots FROM Shots;

SELECT 
    shot_type, 
    COUNT(shot_id) AS total_in_category
FROM Shots
GROUP BY shot_type;