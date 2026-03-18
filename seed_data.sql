INSERT INTO Scenes (scene_id, title, location, shoot_date) 
VALUES (1, 'The Morning Routine', 'Bedroom', '2026-03-19');

INSERT INTO Shots (shot_id, scene_id, description, shot_type, frame_rate) 
VALUES 
(1, 1, 'Actor waking up and stretching', 'A-Roll', 24),
(2, 1, 'Close up of the alarm clock hitting 6:00 AM', 'B-Roll', 60);