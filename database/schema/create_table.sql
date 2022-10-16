DROP DATABASE IF EXISTS zipzup;
CREATE DATABASE zipzup;
USE zipzup;

CREATE TABLE `districts` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `dist_origin` VARCHAR(64) NOT NULL,
    `dist_join` VARCHAR(64) NOT NULL,
    `sub_dist1` VARCHAR(16) NOT NULL, 
    `sub_dist2` VARCHAR(16) NOT NULL,
    `sub_dist3` VARCHAR(16) NOT NULL,
    `sub_dist4` VARCHAR(16),
    PRIMARY KEY (`id`),
    UNIQUE KEY (`dist_origin`)
);
