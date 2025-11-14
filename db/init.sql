CREATE DATABASE IF NOT EXISTS user_db;
USE user_db;
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);
INSERT INTO users (username, password) VALUES ('testuser', 'testpassword');
