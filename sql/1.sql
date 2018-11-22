CREATE TABLE `product` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT NULL,
  `price` int(10) unsigned DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `category_id` int(4) DEFAULT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `category` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`));

ALTER TABLE `product`
ADD INDEX `FK_category_idx` (`category_id` ASC);
;
ALTER TABLE `shop`.`product`
ADD CONSTRAINT `FK_category`
  FOREIGN KEY (`category_id`)
  REFERENCES `shop`.`category` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

 CREATE TABLE `image` (
  `id` int(4) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL;
  PRIMARY KEY (`id`));

