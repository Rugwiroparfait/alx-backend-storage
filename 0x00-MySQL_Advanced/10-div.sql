-- Task: Create a function SafeDiv that divides the first number by the second number, returning 0 if the second number is 0.

-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the SafeDiv function
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    -- Check if the second number (b) is 0, return 0 if true, otherwise return a / b
    RETURN IF(b = 0, 0, a / b);
END;

-- End of the script