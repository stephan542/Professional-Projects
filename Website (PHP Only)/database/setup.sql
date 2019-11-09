CREATE DATABASE ServerDatabaseSw00;
GRANT CREATE,DELETE,DROP,UPDATE,SELECT,INSERT ON ServerDatabaseSw00 TO 'GrinchUWI'@'localhost' IDENTIFIED BY 'stephan97';
CREATE TABLE Users(
	id INT AUTO_INCREMENT,
	firstname VARCHAR(30) NOT NULL,
	lastname VARCHAR(30) NOT NULL,
	gender VARCHAR(7),
	dob DATE NOT NULL,
	username VARCHAR(30) NOT NULL,
	email VARCHAR(60),
	password_digest VARCHAR(64) NOT NULL,
    	last_login DATETIME,
    	failed_login INT,
	salt INT NOT NULL,
    	PRIMARY KEY (id)
)AUTO_INCREMENT=3148;
