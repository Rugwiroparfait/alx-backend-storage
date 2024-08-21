-- Task: Create a table `users` with the specified attributes
-- This script creates the `users` table if it doesn't already exist, 
-- with the following attributes: id, email, name, and country.

-- Create the `users` table with constraints
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, -- ID: Integer, Primary Key, Auto Increment, Never Null
    email VARCHAR(255) NOT NULL UNIQUE,         -- Email: String, 255 characters, Unique, Never Null
    name VARCHAR(255),                          -- Name: String, 255 characters
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US' -- Country: Enum (US, CO, TN), Never Null, Default 'US'
);

-- End of the script.
