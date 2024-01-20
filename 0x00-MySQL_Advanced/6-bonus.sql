-- Drop the existing procedure if it exists
DROP PROCEDURE IF EXISTS AddBonus;

-- Creating a Stored procedure AddBonus
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name varchar(255), IN score INT)
BEGIN
	DECLARE project_id INT;

	-- Check if the project already exists
        SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;

	-- If the project doesn't exists. create it
        IF project_id IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET project_id = LAST_INSERT_ID();
	END IF;

	-- Add the correction for the student
        INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END;
//
DELIMITER ;
