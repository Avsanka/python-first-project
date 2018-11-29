START TRANSACTION;

ALTER TABLE `shop`.`image`
ADD COLUMN `product_id` INT(4) NOT NULL AFTER `url`,
ADD INDEX `fk_image_product1_idx` (`product_id` ASC);

ALTER TABLE `shop`.`image`;
ADD CONSTRAINT `fk_image_product1`
  FOREIGN KEY (`product_id`)
  REFERENCES `shop`.`product` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

COMMIT;