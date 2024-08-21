-- Task: Create a trigger to decrease the quantity of an item after adding a new order.
-- This script creates a trigger that updates the quantity in the items table whenever a new order is inserted.

-- Drop existing trigger if it exists
DROP TRIGGER IF EXISTS decrease_item_quantity;

-- Change the delimiter to $$
DELIMITER $$

-- Create trigger to update item quantity
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update the quantity of the item in the items table
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

-- Reset the delimiter to ;
DELIMITER ;