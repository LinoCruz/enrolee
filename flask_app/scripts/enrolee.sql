-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema enrolee
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema enrolee
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `enrolee` DEFAULT CHARACTER SET utf8 ;
USE `enrolee` ;

-- -----------------------------------------------------
-- Table `enrolee`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `enrolee`.`users` ;

CREATE TABLE IF NOT EXISTS `enrolee`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(200) NULL,
  `last_name` VARCHAR(200) NULL,
  `email` VARCHAR(250) NULL,
  `password` VARCHAR(250) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enrolee`.`events`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `enrolee`.`events` ;

CREATE TABLE IF NOT EXISTS `enrolee`.`events` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(250) NULL,
  `description` TEXT NULL,
  `host` VARCHAR(250) NULL,
  `location` TEXT NULL,
  `cost` VARCHAR(150) NULL,
  `date` DATETIME NULL,
  `time` TIME NULL,
  `registration` TEXT NULL,
  `image` VARCHAR(150) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_events_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_events_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `enrolee`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enrolee`.`speakers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `enrolee`.`speakers` ;

CREATE TABLE IF NOT EXISTS `enrolee`.`speakers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(150) NULL,
  `last_name` VARCHAR(150) NULL,
  `cv` VARCHAR(200) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `event_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_speakers_events1_idx` (`event_id` ASC) VISIBLE,
  CONSTRAINT `fk_speakers_events1`
    FOREIGN KEY (`event_id`)
    REFERENCES `enrolee`.`events` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enrolee`.`assistans_events`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `enrolee`.`assistans_events` ;

CREATE TABLE IF NOT EXISTS `enrolee`.`assistans_events` (
  `user_id` INT NOT NULL,
  `event_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `event_id`),
  INDEX `fk_users_has_events_events1_idx` (`event_id` ASC) VISIBLE,
  INDEX `fk_users_has_events_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_events_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `enrolee`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_events_events1`
    FOREIGN KEY (`event_id`)
    REFERENCES `enrolee`.`events` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enrolee`.`tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `enrolee`.`tags` ;

CREATE TABLE IF NOT EXISTS `enrolee`.`tags` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `event_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tags_events1_idx` (`event_id` ASC) VISIBLE,
  CONSTRAINT `fk_tags_events1`
    FOREIGN KEY (`event_id`)
    REFERENCES `enrolee`.`events` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
