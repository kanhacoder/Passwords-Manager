CREATE DATABASE passwordsDB;
USE passwordsDB;

CREATE TABLE profile_id (
    profile_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    master_password VARCHAR(255) NOT NULL
);

CREATE TABLE passwords (
    password_id INT AUTO_INCREMENT PRIMARY KEY,
    profile_id INT NOT NULL,
    website VARCHAR(100) NOT NULL,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    FOREIGN KEY (profile_id) REFERENCES profile_id(profile_id)
);