-- script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
  -- declare two variables to store the total weighted score and the total weight
  DECLARE tot_weighted_score INT DEFAULT 0;
  DECLARE tot_weight INT DEFAULT 0;
  
  -- calculate the total weighted score by multiplying the score and the weight of each project
  -- and summing them up for the given user_id
  SELECT SUM(corrections.score * projects.weight) INTO tot_weighted_score
  FROM corrections INNER JOIN projects ON corrections.project_id = projects.id
  WHERE corrections.user_id = user_id;
  
  -- calculate the total weight by summign up the weight of each project for the given usre_id
  SELECT SUM(projects.weight) INTO tot_weight FROM corrections INNER JOIN projects ON corrections.project_id = projects.id
  WHERE corrections.user_id = user_id;

  -- check if the total weight is zero to avoid division by zero error
  IF tot_weight = 0 THEN

    -- set the average score to zero to avoid division by zero error
    UPDATE users
    SET users.average_score = 0
    WHERE users.id = user_id;
  ELSE

    -- calculate the average score by dividing the total weighted score by the total weight
    -- and update the users table for the given user_id
    UPDATE users SET users.average_score = tot_weighted_score / tot_weight
    WHERE users.id = user_id;
  END IF;
END //
DELIMITER ;
