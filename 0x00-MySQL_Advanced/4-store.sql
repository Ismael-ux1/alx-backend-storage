-- Creates a trigger named 'after_order_insert' that runs,
-- automatically after a new row is inserted into the 'order' table.


-- Set the dellimeter to // handle the semicolon with in the trigger
DELIMITER //

-- Create a trigger named 'after_order_insert' that activates,
-- AFTER an INSERT operation on the 'orders' table.

CREATE TRIGGER after_order_insert
AFTER INSERT
ON orders FOR EACH ROW
BEGIN
	-- Inside the trigger, update the 'quantity' in the 'items' table.
        
	-- Decrease the quantity by the amount specified in the,
	-- newly inserted row in the 'orders' table
        UPDATE items
	SET quantity = quantity - NEW.quantity
	WHERE item_id = NEW.item_id;
END; //

-- Reset the delimeter back to the default semicolon.
DELIMITER ;
