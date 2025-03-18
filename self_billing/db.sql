/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.22 : Database - self_billing
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`self_billing` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `self_billing`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add deliveryboy',7,'add_deliveryboy'),
(26,'Can change deliveryboy',7,'change_deliveryboy'),
(27,'Can delete deliveryboy',7,'delete_deliveryboy'),
(28,'Can view deliveryboy',7,'view_deliveryboy'),
(29,'Can add login',8,'add_login'),
(30,'Can change login',8,'change_login'),
(31,'Can delete login',8,'delete_login'),
(32,'Can view login',8,'view_login'),
(33,'Can add notification',9,'add_notification'),
(34,'Can change notification',9,'change_notification'),
(35,'Can delete notification',9,'delete_notification'),
(36,'Can view notification',9,'view_notification'),
(37,'Can add order',10,'add_order'),
(38,'Can change order',10,'change_order'),
(39,'Can delete order',10,'delete_order'),
(40,'Can view order',10,'view_order'),
(41,'Can add product',11,'add_product'),
(42,'Can change product',11,'change_product'),
(43,'Can delete product',11,'delete_product'),
(44,'Can view product',11,'view_product'),
(45,'Can add user',12,'add_user'),
(46,'Can change user',12,'change_user'),
(47,'Can delete user',12,'delete_user'),
(48,'Can view user',12,'view_user'),
(49,'Can add staff',13,'add_staff'),
(50,'Can change staff',13,'change_staff'),
(51,'Can delete staff',13,'delete_staff'),
(52,'Can view staff',13,'view_staff'),
(53,'Can add payment',14,'add_payment'),
(54,'Can change payment',14,'change_payment'),
(55,'Can delete payment',14,'delete_payment'),
(56,'Can view payment',14,'view_payment'),
(57,'Can add orders',15,'add_orders'),
(58,'Can change orders',15,'change_orders'),
(59,'Can delete orders',15,'delete_orders'),
(60,'Can view orders',15,'view_orders'),
(61,'Can add orderdetails',16,'add_orderdetails'),
(62,'Can change orderdetails',16,'change_orderdetails'),
(63,'Can delete orderdetails',16,'delete_orderdetails'),
(64,'Can view orderdetails',16,'view_orderdetails'),
(65,'Can add order_details',17,'add_order_details'),
(66,'Can change order_details',17,'change_order_details'),
(67,'Can delete order_details',17,'delete_order_details'),
(68,'Can view order_details',17,'view_order_details'),
(69,'Can add offers',18,'add_offers'),
(70,'Can change offers',18,'change_offers'),
(71,'Can delete offers',18,'delete_offers'),
(72,'Can view offers',18,'view_offers'),
(73,'Can add location',19,'add_location'),
(74,'Can change location',19,'change_location'),
(75,'Can delete location',19,'delete_location'),
(76,'Can view location',19,'view_location'),
(77,'Can add feedback',20,'add_feedback'),
(78,'Can change feedback',20,'change_feedback'),
(79,'Can delete feedback',20,'delete_feedback'),
(80,'Can view feedback',20,'view_feedback'),
(81,'Can add complaint',21,'add_complaint'),
(82,'Can change complaint',21,'change_complaint'),
(83,'Can delete complaint',21,'delete_complaint'),
(84,'Can view complaint',21,'view_complaint'),
(85,'Can add assign_order',22,'add_assign_order'),
(86,'Can change assign_order',22,'change_assign_order'),
(87,'Can delete assign_order',22,'delete_assign_order'),
(88,'Can view assign_order',22,'view_assign_order');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$0a6JClHLGRrISz9bsop543$O0f7zz/E1JWXlz3ITTDo5/lgCE6XPpGSk933U//oxGo=','2023-12-03 11:15:30.654828',1,'admin','','','admin@gmail.com',1,1,'2023-11-27 05:07:38.189539');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `billing_app_assign_order` */

DROP TABLE IF EXISTS `billing_app_assign_order`;

CREATE TABLE `billing_app_assign_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `DELIVERYBOY_id` bigint NOT NULL,
  `order_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_assign_o_DELIVERYBOY_id_05cbfcec_fk_billing_a` (`DELIVERYBOY_id`),
  KEY `billing_app_assign_o_order_id_c10cd8f7_fk_billing_a` (`order_id`),
  CONSTRAINT `billing_app_assign_o_DELIVERYBOY_id_05cbfcec_fk_billing_a` FOREIGN KEY (`DELIVERYBOY_id`) REFERENCES `billing_app_deliveryboy` (`id`),
  CONSTRAINT `billing_app_assign_o_order_id_c10cd8f7_fk_billing_a` FOREIGN KEY (`order_id`) REFERENCES `billing_app_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_assign_order` */

insert  into `billing_app_assign_order`(`id`,`date`,`status`,`DELIVERYBOY_id`,`order_id`) values 
(3,'2023-12-03','pending',1,9),
(4,'2023-12-03','delivered',2,10);

/*Table structure for table `billing_app_complaint` */

DROP TABLE IF EXISTS `billing_app_complaint`;

CREATE TABLE `billing_app_complaint` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_complaint_USER_id_7cc728ab_fk_billing_app_user_id` (`USER_id`),
  CONSTRAINT `billing_app_complaint_USER_id_7cc728ab_fk_billing_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `billing_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_complaint` */

insert  into `billing_app_complaint`(`id`,`complaint`,`date`,`reply`,`USER_id`) values 
(1,'it is not good','2023-11-27','pending',1);

/*Table structure for table `billing_app_deliveryboy` */

DROP TABLE IF EXISTS `billing_app_deliveryboy`;

CREATE TABLE `billing_app_deliveryboy` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `lati` double NOT NULL,
  `longi` double NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_delivery_LOGIN_id_15089793_fk_billing_a` (`LOGIN_id`),
  CONSTRAINT `billing_app_delivery_LOGIN_id_15089793_fk_billing_a` FOREIGN KEY (`LOGIN_id`) REFERENCES `billing_app_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_deliveryboy` */

insert  into `billing_app_deliveryboy`(`id`,`name`,`Gender`,`place`,`post`,`pin`,`phone`,`email`,`lati`,`longi`,`LOGIN_id`) values 
(1,'rahul','Female','8978987878','kodakunn',768787,9878987898,'rahul@gmail.com',11.2577497,75.7845224,3),
(2,'manas','Male','wayanad','wayanad',656543,9876543232,'manas@gmail.com',11.2577459,75.7845239,9),
(3,'nihal','Male','kollam','kollam',656543,9876543232,'nihal@gmail.com',0,0,11);

/*Table structure for table `billing_app_feedback` */

DROP TABLE IF EXISTS `billing_app_feedback`;

CREATE TABLE `billing_app_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `rating` double NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_feedback_USER_id_df7d171b_fk_billing_app_user_id` (`USER_id`),
  CONSTRAINT `billing_app_feedback_USER_id_df7d171b_fk_billing_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `billing_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_feedback` */

insert  into `billing_app_feedback`(`id`,`feedback`,`date`,`rating`,`USER_id`) values 
(1,'hvv','2023-11-27',2,1);

/*Table structure for table `billing_app_location` */

DROP TABLE IF EXISTS `billing_app_location`;

CREATE TABLE `billing_app_location` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `latitude` bigint NOT NULL,
  `longitude` bigint NOT NULL,
  `DELIVERYBOY_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_location_DELIVERYBOY_id_f823c593_fk_billing_a` (`DELIVERYBOY_id`),
  CONSTRAINT `billing_app_location_DELIVERYBOY_id_f823c593_fk_billing_a` FOREIGN KEY (`DELIVERYBOY_id`) REFERENCES `billing_app_deliveryboy` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_location` */

/*Table structure for table `billing_app_login` */

DROP TABLE IF EXISTS `billing_app_login`;

CREATE TABLE `billing_app_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_login` */

insert  into `billing_app_login`(`id`,`username`,`password`,`type`) values 
(1,'admin','Admin@123','admin'),
(2,'kiran','Kiran@123','staff'),
(3,'rahul','Rahul@123','deliveryboy'),
(4,'athul','12345678','user'),
(5,'aleefa','Aleefa@123','staff'),
(8,'anu','Anu@1234','user'),
(9,'manas','Manas@123','deliveryboy'),
(10,'salha','Salha@123','staff'),
(11,'nihal','Nihal@1234','deliveryboy');

/*Table structure for table `billing_app_notification` */

DROP TABLE IF EXISTS `billing_app_notification`;

CREATE TABLE `billing_app_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `notification` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_notification` */

insert  into `billing_app_notification`(`id`,`notification`,`date`) values 
(2,'   all-staff meeting is scheduled for 9 o\'clock.    ','2023-11-27');

/*Table structure for table `billing_app_offers` */

DROP TABLE IF EXISTS `billing_app_offers`;

CREATE TABLE `billing_app_offers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `offers` int NOT NULL,
  `details` varchar(100) NOT NULL,
  `fromdate` date NOT NULL,
  `todate` date NOT NULL,
  `type` varchar(100) NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_offers_PRODUCT_id_8ae9f895_fk_billing_app_product_id` (`PRODUCT_id`),
  CONSTRAINT `billing_app_offers_PRODUCT_id_8ae9f895_fk_billing_app_product_id` FOREIGN KEY (`PRODUCT_id`) REFERENCES `billing_app_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_offers` */

insert  into `billing_app_offers`(`id`,`offers`,`details`,`fromdate`,`todate`,`type`,`PRODUCT_id`) values 
(1,1,'monthend','2023-11-29','2023-11-30','Buy One, Get One',2),
(2,2,'frftddd','2023-11-30','2023-11-29','Flat offers',4),
(3,0,'hjk','2023-12-05','2023-12-28','Buy One, Get One',2),
(4,2,'fghj','2023-12-27','2023-12-14','Buy One, Get One',2);

/*Table structure for table `billing_app_order` */

DROP TABLE IF EXISTS `billing_app_order`;

CREATE TABLE `billing_app_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `ordertype` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_order_USER_id_d78da521_fk_billing_app_user_id` (`USER_id`),
  CONSTRAINT `billing_app_order_USER_id_d78da521_fk_billing_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `billing_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_order` */

insert  into `billing_app_order`(`id`,`amount`,`date`,`status`,`ordertype`,`USER_id`) values 
(9,210,'2023-12-03','PAID','online',1),
(10,80,'2023-12-03','PAID','online',1),
(11,10,'2023-12-03','PAID','online',1);

/*Table structure for table `billing_app_order_details` */

DROP TABLE IF EXISTS `billing_app_order_details`;

CREATE TABLE `billing_app_order_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `date` date NOT NULL,
  `ORDER_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_order_de_ORDER_id_00c16cf7_fk_billing_a` (`ORDER_id`),
  KEY `billing_app_order_de_PRODUCT_id_69ca9a4f_fk_billing_a` (`PRODUCT_id`),
  CONSTRAINT `billing_app_order_de_ORDER_id_00c16cf7_fk_billing_a` FOREIGN KEY (`ORDER_id`) REFERENCES `billing_app_orders` (`id`),
  CONSTRAINT `billing_app_order_de_PRODUCT_id_69ca9a4f_fk_billing_a` FOREIGN KEY (`PRODUCT_id`) REFERENCES `billing_app_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_order_details` */

/*Table structure for table `billing_app_orderdetails` */

DROP TABLE IF EXISTS `billing_app_orderdetails`;

CREATE TABLE `billing_app_orderdetails` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `ORDER_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_orderdet_ORDER_id_f82349cd_fk_billing_a` (`ORDER_id`),
  KEY `billing_app_orderdet_PRODUCT_id_d7745fac_fk_billing_a` (`PRODUCT_id`),
  CONSTRAINT `billing_app_orderdet_ORDER_id_f82349cd_fk_billing_a` FOREIGN KEY (`ORDER_id`) REFERENCES `billing_app_order` (`id`),
  CONSTRAINT `billing_app_orderdet_PRODUCT_id_d7745fac_fk_billing_a` FOREIGN KEY (`PRODUCT_id`) REFERENCES `billing_app_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_orderdetails` */

insert  into `billing_app_orderdetails`(`id`,`quantity`,`ORDER_id`,`PRODUCT_id`) values 
(10,2,9,4),
(11,4,9,5),
(12,2,10,5),
(13,2,11,2);

/*Table structure for table `billing_app_orders` */

DROP TABLE IF EXISTS `billing_app_orders`;

CREATE TABLE `billing_app_orders` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `price` int NOT NULL,
  `username` varchar(156) NOT NULL,
  `phone` varchar(568) NOT NULL,
  `STAFF_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_orders_STAFF_id_c050c071_fk_billing_app_staff_id` (`STAFF_id`),
  CONSTRAINT `billing_app_orders_STAFF_id_c050c071_fk_billing_app_staff_id` FOREIGN KEY (`STAFF_id`) REFERENCES `billing_app_staff` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_orders` */

/*Table structure for table `billing_app_payment` */

DROP TABLE IF EXISTS `billing_app_payment`;

CREATE TABLE `billing_app_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `ORDER_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_payment_ORDER_id_97183a4e_fk_billing_app_order_id` (`ORDER_id`),
  KEY `billing_app_payment_USER_id_cca6ebe7_fk_billing_app_user_id` (`USER_id`),
  CONSTRAINT `billing_app_payment_ORDER_id_97183a4e_fk_billing_app_order_id` FOREIGN KEY (`ORDER_id`) REFERENCES `billing_app_order` (`id`),
  CONSTRAINT `billing_app_payment_USER_id_cca6ebe7_fk_billing_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `billing_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_payment` */

insert  into `billing_app_payment`(`id`,`amount`,`date`,`status`,`ORDER_id`,`USER_id`) values 
(6,210,'2023-12-03','PAID',9,1),
(7,80,'2023-12-03','PAID',10,1),
(8,10,'2023-12-03','PAID',11,1);

/*Table structure for table `billing_app_product` */

DROP TABLE IF EXISTS `billing_app_product`;

CREATE TABLE `billing_app_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `productname` varchar(100) NOT NULL,
  `Description` longtext NOT NULL,
  `Company` varchar(100) NOT NULL,
  `Category` varchar(100) NOT NULL,
  `qr` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `stock` int NOT NULL,
  `price` double NOT NULL,
  `Manufacturingdate` date NOT NULL,
  `Expirydate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_product` */

insert  into `billing_app_product`(`id`,`productname`,`Description`,`Company`,`Category`,`qr`,`image`,`stock`,`price`,`Manufacturingdate`,`Expirydate`) values 
(2,'Lay\'s Classic Potato Chips','Thick-cut, kettle-cooked potato chips with a touch of sea salt for a hearty and crunchy texture.','Lay\'s','Snacks','media/qr/2.png','lays.jpg',194,5,'2023-11-27','2024-11-26'),
(3,'Bread','Soft multigrain roll with sunflower seeds for a delightful nutty taste and added crunch.',' Nature\'s Harvest Breads',' Bakery','media/qr/3.png','bread.jpg',0,42,'2023-11-27','2024-01-25'),
(4,' Milk','Low-fat milk option with reduced fat content while retaining essential nutrients.','Milma ',' Dairy','media/qr/4.png','milma-nandini.jpg',296,25,'2023-11-27','2023-12-26'),
(5,' ChocoChips Bliss Biscuits','Chocolate chip biscuits with a perfect balance of sweetness and rich chocolate flavor.','Delightful Bites ','Backery','media/qr/5.png','biscuits.png',21,40,'2023-11-27','2024-11-26'),
(6,'Chocolate Fudge Fantasy','Smooth and creamy vanilla ice cream made with real vanilla beans for a rich and indulgent flavor.',' Vanilla ice cream ',' Ice Cream/','media/qr/6.png','icecream.jpeg',47,15,'2023-11-27','2023-12-26'),
(7,'Aloe Vera Hydration Bar',' Hydrating soap bar infused with aloe vera for moisturizing and soothing the skin.','Herbal Shield Soaps',' Personal Care','media/qr/7.png','soap.jpeg',98,23,'2023-11-27','2026-07-21'),
(8,' SilkSmooth Shampoo','silk proteins for smooth and silky hair, suitable for daily use.',' LuxeLocks Care','personal  care','media/qr/8.png','shampoo.jpeg',30,56,'2023-11-27','2025-11-26');

/*Table structure for table `billing_app_staff` */

DROP TABLE IF EXISTS `billing_app_staff`;

CREATE TABLE `billing_app_staff` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_staff_LOGIN_id_095a603e_fk_billing_app_login_id` (`LOGIN_id`),
  CONSTRAINT `billing_app_staff_LOGIN_id_095a603e_fk_billing_app_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `billing_app_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_staff` */

insert  into `billing_app_staff`(`id`,`fname`,`lname`,`gender`,`place`,`post`,`pin`,`phone`,`email`,`photo`,`LOGIN_id`) values 
(1,'kiran','kumar','Male','kodayam','kollam',657656,9878678798,'kiran@gmail.com','man stafff.png',2),
(2,'aleefa','mp','Female','mukkam','mukkam',655543,9876543212,'aleefa@gmail.com','ladystaff.jpg',5),
(5,'fathima','salha','Female','calicut','calicut',656541,8765454343,'salha@hmail.com','ladystaff_yLYOaQ8.jpg',10);

/*Table structure for table `billing_app_user` */

DROP TABLE IF EXISTS `billing_app_user`;

CREATE TABLE `billing_app_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_app_user_LOGIN_id_ed8be001_fk_billing_app_login_id` (`LOGIN_id`),
  CONSTRAINT `billing_app_user_LOGIN_id_ed8be001_fk_billing_app_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `billing_app_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `billing_app_user` */

insert  into `billing_app_user`(`id`,`name`,`photo`,`place`,`post`,`pin`,`phone`,`email`,`LOGIN_id`) values 
(1,'athul','Screenshot_20230218-143550.png','tamilnadu ','sellam',678789,9878987898,'athul@gmail.com',4),
(2,'anu','IMG-20230820-WA0032.jpg','koduvally','koduvally',657654,9876765454,'anu@gmail.com',8);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(22,'billing_app','assign_order'),
(21,'billing_app','complaint'),
(7,'billing_app','deliveryboy'),
(20,'billing_app','feedback'),
(19,'billing_app','location'),
(8,'billing_app','login'),
(9,'billing_app','notification'),
(18,'billing_app','offers'),
(10,'billing_app','order'),
(17,'billing_app','order_details'),
(16,'billing_app','orderdetails'),
(15,'billing_app','orders'),
(14,'billing_app','payment'),
(11,'billing_app','product'),
(13,'billing_app','staff'),
(12,'billing_app','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-11-27 05:05:59.527323'),
(2,'auth','0001_initial','2023-11-27 05:06:00.822946'),
(3,'admin','0001_initial','2023-11-27 05:06:01.300600'),
(4,'admin','0002_logentry_remove_auto_add','2023-11-27 05:06:01.327595'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-11-27 05:06:01.352182'),
(6,'contenttypes','0002_remove_content_type_name','2023-11-27 05:06:01.559361'),
(7,'auth','0002_alter_permission_name_max_length','2023-11-27 05:06:01.695069'),
(8,'auth','0003_alter_user_email_max_length','2023-11-27 05:06:01.753572'),
(9,'auth','0004_alter_user_username_opts','2023-11-27 05:06:01.772688'),
(10,'auth','0005_alter_user_last_login_null','2023-11-27 05:06:01.901836'),
(11,'auth','0006_require_contenttypes_0002','2023-11-27 05:06:01.911062'),
(12,'auth','0007_alter_validators_add_error_messages','2023-11-27 05:06:01.934802'),
(13,'auth','0008_alter_user_username_max_length','2023-11-27 05:06:02.183253'),
(14,'auth','0009_alter_user_last_name_max_length','2023-11-27 05:06:02.347010'),
(15,'auth','0010_alter_group_name_max_length','2023-11-27 05:06:02.429767'),
(16,'auth','0011_update_proxy_permissions','2023-11-27 05:06:02.449826'),
(17,'auth','0012_alter_user_first_name_max_length','2023-11-27 05:06:02.569178'),
(18,'billing_app','0001_initial','2023-11-27 05:06:06.416764'),
(19,'sessions','0001_initial','2023-11-27 05:06:06.516671');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('6r8n01ihg7hzop4pakhdw1pxf8irio26','.eJxVTjkOwjAQ_IvryLITHxtKesQTorV3IYEojnJUiL9joxRQzWguzUt0uG99t6-8dAOJk9Ci-tUCxidPxaAHTvckY5q2ZQiyROThrvKSiMfzkf0b6HHtc9tzEw0gsQ6OgzdOUSQHAKHF1noLqjZIxAr8DRSEGska69E3Vhnd1nl0LP90Ja5fzGQuxLw_qRU92w:1r9kRe:NLG5oL2Q70lkwIvj-5gZLRDvXz9EBBzv05bwuOEa6Ek','2023-12-17 11:15:30.694334'),
('n4sdf8dlsj8dicmyckmw972uvna9xzje','.eJxVjs0OwiAQhN-FMyFAoWw9ejc-QrOwq1SbtunPyfjuFtODniaZ-WYyL9HituZ2W3huOxInYYT89SKmJw8loAcO91GlcVjnLqqCqCNd1GUk7s8H-zeQccl7O3CVHCCxiTXH4GpNiWoAiA02PnjQ1iERawg30BAtknc-YKi8dqax-2hf_lkppqJGiutX3x9tLT2o:1r7Ute:pqheGeR4ysBwKZryO8jqZCffUCOJpP_sM1GeOdDHh7o','2023-12-11 06:15:06.340885'),
('pzat7pb0n201i9qg1qnt3j5kju2ycki3','.eJxVjsEOwiAQRP-FsyFAoWw9eu83kIVdpdrQpLQn479bkh70Om_mZd4i4L7lsFdew0TiKrS4_GYR04tLA_TE8lhkWsq2TlG2ijxpleNCPN_O7p8gY83H2nOXLCCxjj1Hb3tFiXoAiAMOzjtQxiIRK_B3UBANkrPOo--csnowh3Ru_9znC7QCOZw:1r9eeZ:QIc1rz4OpvpXSiPCt0mjDrBK5QCg3IGgioz4doGiLMM','2023-12-17 05:04:27.359826');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
