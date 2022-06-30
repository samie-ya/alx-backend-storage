-- This script will create a stored procedure called ComputeAverageScoreForUser
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
NOT DETERMINISTIC
BEGIN
	DECLARE total INT;
	DECLARE amount INT;
	DECLARE ave FLOAT;
	SELECT SUM(score) INTO total  FROM corrections WHERE corrections.user_id = user_id;
	SELECT COUNT(score) INTO amount  FROM corrections WHERE corrections.user_id = user_id;
	SET ave = total / amount;
	UPDATE users SET average_score = ave WHERE id = user_id;
END//
DELIMITER ;//
