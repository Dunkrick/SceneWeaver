CREATE TABLE Scenes (
    scene_id INT PRIMARY KEY, 
    title TEXT NOT NULL, 
    location TEXT, 
    shoot_date DATE
);

CREATE TABLE Shots (
    shot_id INT AUTO_INCREMENT PRIMARY KEY, 
    scene_id INT,                      
    description TEXT, 
    shot_type TEXT CHECK (shot_type IN ('A-Roll', 'B-Roll', 'Screen Recording')), 
    frame_rate INT, 
    Shot_status BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (scene_id) REFERENCES Scenes(scene_id) 
);