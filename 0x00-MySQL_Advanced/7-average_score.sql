-- Creating a Stored Procedure ComputeAverageScoreForUser
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Set delimiter
DELIMITER //
-- Create procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	-- Update average_score in users table with the average score,
        -- from correction table for the given user_id
        UPDATE users
	SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
	WHERE id = user_id;
END;
//
DELIMITER ;
