CREATE database internet_shop_1;
USE internet_shop_1;

CREATE TABLE `user` (
	`user_id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`user_password` varchar(25) NOT NULL,
	`user_login` varchar(25) NOT NULL,
	`user_email` varchar(30),
	`user_about` varchar(1000),
	`user_first_name` varchar(10) NOT NULL,
	`user_second_name` varchar(20) NOT NULL,
	PRIMARY KEY (`user_id`)
);

CREATE TABLE `storage` (
	`storage_id` INT NOT NULL AUTO_INCREMENT,
	`storage_adress_city` VARCHAR(50) NOT NULL,
	`storage_rental_price` INT NOT NULL,
	`storage_adress_street` VARCHAR(50) NOT NULL,
	`storage_adress_house` VARCHAR(50) NOT NULL,
	PRIMARY KEY (`storage_id`)
);

CREATE TABLE `comment` (
	`comment_id` INT NOT NULL,
	`comment_text` varchar(1000),
	`comment_time` DATETIME NOT NULL,
	`comment_mark` INT,
	PRIMARY KEY (`comment_id`)
);

CREATE TABLE `delivery_service` (
	`delivery_service_id` INT NOT NULL AUTO_INCREMENT,
	`delivery_service_prices` INT NOT NULL,
	`delivery_service_about` VARCHAR(1000) NOT NULL,
	PRIMARY KEY (`delivery_service_id`)
);

CREATE TABLE `product` (
	`product_id` INT NOT NULL AUTO_INCREMENT,
	`storage_id` INT NOT NULL,
	`product_info` varchar(1000) NOT NULL,
	`product_price` INT NOT NULL,
	`product_theme` varchar(255),
	PRIMARY KEY (`product_id`),
    CONSTRAINT `product_fk0` FOREIGN KEY (`storage_id`) REFERENCES `storage`(`storage_id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `active_goods` (
	`active_goods_id` INT NOT NULL AUTO_INCREMENT,
	`product_id` INT NOT NULL,
	`delivery_service_id` INT NOT NULL,
	`sell/buy` BINARY NOT NULL,
	`comment_id` INT unique,
	`activate_time` DATETIME NOT NULL,
	`arrive_address_city` varchar(20) NOT NULL,
	`arrive_address_street` varchar(20) NOT NULL,
	`arrive_address_house` varchar(20) NOT NULL,
	PRIMARY KEY (`active_goods_id`),
	CONSTRAINT `active_goods_fk2` FOREIGN KEY (`comment_id`) REFERENCES `comment`(`comment_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `active_goods_fk1` FOREIGN KEY (`delivery_service_id`) REFERENCES `delivery_service`(`delivery_service_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `active_goods_fk0` FOREIGN KEY (`product_id`) REFERENCES `product`(`product_id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `basket` (
	`user_id` INT NOT NULL,
	`product_id` INT NOT NULL,
	`product_amount` INT,
	`basket_name` varchar(20) NOT NULL,
    CONSTRAINT `basket_fk0` FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `basket_fk1` FOREIGN KEY (`product_id`) REFERENCES `product`(`product_id`)  ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `list_active_goods` (
	`user_id` INT NOT NULL,
	`active_goods_id` INT NOT NULL,
    CONSTRAINT `list_active_goods_fk0` FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `list_active_goods_fk1` FOREIGN KEY (`active_goods_id`) REFERENCES `active_goods`(`active_goods_id`) ON DELETE CASCADE ON UPDATE CASCADE
);