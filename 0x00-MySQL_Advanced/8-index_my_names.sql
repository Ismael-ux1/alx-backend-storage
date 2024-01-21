-- Add a new column for the first letter of the name
ALTER TABLE names ADD COLUMN first_letter CHAR(1);

-- Update the new column with the first letter of the name
UPDATE names SET first_letter = SUBSTRING(name, 1, 1);

-- Create the index on the new column
CREATE INDEX idx_name_first ON names(first_letter);
