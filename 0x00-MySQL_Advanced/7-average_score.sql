-- Task: Create a stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student.

-- Drop the stored procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Change the delimiter to $$
DELIMITER $$

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END$$

-- Reset the delimiter to ;
DELIMITER ;
