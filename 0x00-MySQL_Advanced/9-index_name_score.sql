-- Optimize search and score
-- Create index 'idx_name_first_score' on first letter of 'name' and 'score'
CREATE INDEX idx_name_first_score ON names (name(1), score);
