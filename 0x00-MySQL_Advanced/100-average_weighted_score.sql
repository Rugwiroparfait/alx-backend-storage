-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;

    -- Calculate the total weighted score and total weight for the user
    SELECT 
        SUM(c.score * p.weight), 
        SUM(p.weight)
    INTO 
        total_weighted_score, 
        total_weight
    FROM 
        corrections c
    JOIN 
        projects p ON c.project_id = p.id
    WHERE 
        c.user_id = user_id;

    -- If total_weight is not zero, update the average_score in users table
    IF total_weight > 0 THEN
        UPDATE users
        SET average_score = total_weighted_score / total_weight
        WHERE id = user_id;
    END IF;

END //

DELIMITER ;
