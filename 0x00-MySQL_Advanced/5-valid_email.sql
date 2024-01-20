-- Create a trigger named 'reset_valid_email' to reset 'valid_email',
-- When email is changed

DELIMITER //
CREATE TRIGGER reset_valid_email
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
	-- Check if the 'email' column is being updated
        IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;//
DELIMITER ;
