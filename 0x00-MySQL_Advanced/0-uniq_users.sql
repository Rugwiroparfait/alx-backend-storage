-- Task: Create a table `users` with the specified attributes
-- This script creates the `users` table if it doesn't already exist, 
-- with the following attributes: id, email, and name.

-- Create the `users` table with constraints
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,           -- ID: Integer, Auto Increment, Never Null
    email VARCHAR(255) NOT NULL UNIQUE,       -- Email: String, 255 characters, Unique, Never Null
    name VARCHAR(255),                        -- Name: String, 255 characters
    PRIMARY KEY (id)                          -- Primary Key on `id`
);

-- End of the script.