-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    
    -- Declare a cursor for the users
    DECLARE user_cursor CURSOR FOR 
    SELECT id FROM users;
    
    -- Declare a handler to set the done variable when the cursor is exhausted
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    
    -- Open the cursor
    OPEN user_cursor;
    
    -- Loop through all users
    read_loop: LOOP
        -- Fetch the next user id
        FETCH user_cursor INTO user_id;
        
        -- If no more rows, exit the loop
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Calculate and update the average weighted score for the current user
        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;
    
    -- Close the cursor
    CLOSE user_cursor;
END //

DELIMITER ;
