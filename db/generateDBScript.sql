CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Locations` (
  `id` INT NOT NULL,
  `name` VARCHAR(60) NOT NULL,
  `description` VARCHAR(200) NULL,
  `location_parent_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `locations_location_parent_id_fkx` (`location_parent_id` ASC) INVISIBLE,
  INDEX `locations_namex` (`name` ASC) VISIBLE,
  CONSTRAINT `locations_location_parent_id_fk`
    FOREIGN KEY (`location_parent_id`)
    REFERENCES `mydb`.`Locations` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`Articles` (
  `id` INT NOT NULL,
  `name` VARCHAR(60) NOT NULL,
  `description` VARCHAR(200) NOT NULL,
  `location_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `articles_location_fkx` (`location_id` ASC) VISIBLE,
  INDEX `articles_namex` (`name` ASC) VISIBLE,
  CONSTRAINT `articles_location_fk`
    FOREIGN KEY (`location_id`)
    REFERENCES `mydb`.`Locations` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
