-- Task: Create a trigger to reset the valid_email attribute when the email is changed.
-- This script creates a trigger that sets valid_email to 0 if the email is updated.

-- Drop existing trigger if it exists
DROP TRIGGER IF EXISTS reset_valid_email_on_email_change;

-- Change the delimiter to $$
DELIMITER $$

-- Create the trigger
CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email has been changed
    IF OLD.email <> NEW.email THEN
        -- Reset valid_email to 0 if the email has been changed
        SET NEW.valid_email = 0;
    END IF;
END$$

-- Reset the delimiter to ;
DELIMITER ;