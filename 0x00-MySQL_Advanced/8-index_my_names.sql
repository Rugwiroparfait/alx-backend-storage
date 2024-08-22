-- Task: Create an index idx_name_first on the table names, indexing only the first letter of name.

-- Drop the index if it already exists
DROP INDEX IF EXISTS idx_name_first ON names;

-- Create the index idx_name_first on the first letter of the name column
CREATE INDEX idx_name_first ON names (name(1));

-- End of the script
