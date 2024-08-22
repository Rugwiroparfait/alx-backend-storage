-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Open cursor for iterating over each user
    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate the total weighted score and total weight for the current user
        CALL ComputeAverageWeightedScoreForUser(user_id);
        
    END LOOP;

    CLOSE cur;

END //

DELIMITER ;
