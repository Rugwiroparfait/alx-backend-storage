-- Task: Create a view need_meeting that lists all students with a score under 80 and either no last_meeting date or a last_meeting date more than a month ago.

-- Drop the view if it already exists
DROP VIEW IF EXISTS need_meeting;

-- Create the need_meeting view
CREATE VIEW need_meeting AS
SELECT 
    name
FROM 
    students
WHERE 
    score < 80
    AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);

-- End of script
