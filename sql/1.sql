CREATE TABLE `product` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT NULL,
  `price` int(10) unsigned DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `category_id` int(4) DEFAULT NULL,
  PRIMARY KEY (`id`)

