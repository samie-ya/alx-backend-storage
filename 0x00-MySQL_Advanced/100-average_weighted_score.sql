-- This script will create a stored procedure called
-- ComputeAverageWeightedScoreForUser
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
NOT DETERMINISTIC
BEGIN
	DECLARE product INT;
	DECLARE total INT;
	DECLARE ave FLOAT;
	SELECT SUM(projects.weight * corrections.score) INTO product
	FROM projects
	INNER JOIN corrections
	ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;
	SELECT SUM(projects.weight) INTO total
	FROM projects
	INNER JOIN corrections
	ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;
	SET ave = product / total;
	UPDATE users SET average_score = ave WHERE id = user_id;
END//
DELIMITER ;//
