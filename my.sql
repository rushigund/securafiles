CREATE DATABASE login DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE login;
CREATE TABLE accounts (
    id INT(100) NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    mypassword VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
)  ENGINE=INNODB AUTO_INCREMENT=2 DEFAULT CHARSET=UTF8;