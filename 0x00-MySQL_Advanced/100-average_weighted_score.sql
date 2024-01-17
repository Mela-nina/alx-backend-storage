-- This is a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month

DROP procedure IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
	IN user_id INT
)
BEGIN
    UPDATE users
   	SET average_score=(SELECT AVG(score) FROM corrections
			     WHERE corrections.user_id=user_id)
	WHERE id=user_id;
END;
|
