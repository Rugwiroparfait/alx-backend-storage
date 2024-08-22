-- Task: Create an index idx_name_first_score on the table names, indexing only the first letter of name and the score.

-- Drop the index if it already exists
DROP INDEX IF EXISTS idx_name_first_score ON names;

-- Create the index idx_name_first_score on the first letter of name and score
CREATE INDEX idx_name_first_score ON names (name(1), score);

-- End of the script
