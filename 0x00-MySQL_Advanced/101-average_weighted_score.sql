-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
  -- declare a variable to store the current user id
  DECLARE user_id INT;
  -- declare a variable to indicate the end of the cursor
  DECLARE done INT DEFAULT FALSE;

  -- declare a cursor to loop through all users
  DECLARE user_cursor CURSOR FOR SELECT id FROM users;
  -- declare a handler to set done to true when the cursor reaches the end
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  -- open the cursor
  OPEN user_cursor;

  -- start the loop
  user_loop: LOOP
    -- fetch the next user id from the cursor
    FETCH user_cursor INTO user_id;
    -- exit the loop if done is true
    IF done THEN
      LEAVE user_loop;
    END IF;
    -- call the stored procedure ComputeAverageWeightedScoreForUser for the current user id
    CALL ComputeAverageWeightedScoreForUser (user_id);
  END LOOP;

  -- close the cursor
  CLOSE user_cursor;
END //
DELIMITER ;
