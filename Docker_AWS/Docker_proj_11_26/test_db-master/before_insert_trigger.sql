DROP TRIGGER IF EXISTS salary_round;
DELIMITER $$
CREATE TRIGGER salary_round BEFORE INSERT ON salaries
FOR EACH ROW
	BEGIN   
		        SET NEW.salary=ROUND(NEW.salary);
		END
		$$
		DELIMITER ;
