-- This script will create index using score and the first index of name
CREATE INDEX idx_name_first_score ON names (name(1), score);
