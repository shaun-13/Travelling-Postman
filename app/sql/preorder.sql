-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 29, 2020 at 04:17 PM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

DROP DATABASE IF EXISTS preorder;
CREATE DATABASE IF NOT EXISTS preorder;
USE preorder;


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `preorder`
--

-- --------------------------------------------------------

--
-- Table structure for table `preorder_details`
--

DROP TABLE IF EXISTS `preorder_details`;
CREATE TABLE IF NOT EXISTS `preorder_details` (
  `po_id` int(10) NOT NULL AUTO_INCREMENT,
  `traveller_id` varchar(100) CHARACTER SET utf8 NOT NULL,
  `country` varchar(80) CHARACTER SET utf8 NOT NULL,
  `end_date` date NOT NULL,
  `item_name` varchar(100) CHARACTER SET utf8 NOT NULL,
  `item_category` varchar(100) CHARACTER SET utf8 NOT NULL,
  `price` decimal(8,2) NOT NULL,
  PRIMARY KEY (`po_id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `preorder_details`
--

INSERT INTO `preorder_details` (`po_id`, `traveller_id`, `country`, `end_date`, `item_name`, `item_category`, `price`) VALUES
(1, '333', 'Iceland', '2019-01-01', 'Chinese Bowl', 'Vintage Goods', '23.20'),
(11, '333', 'Norway', '2020-05-01', 'Salmon', 'Food and Beverages', '44.50'),
(12, '333', 'Japan', '2020-04-01', 'Naruto Figurine', 'Toys', '20.45'),
(55, '100', 'Brazil', '2020-07-11', 'Limited Edition Gucci Laptop Cover SS20', "Books and Stationery", '750'),
(56, '100', 'Australia', '2020-04-29', "Talking Kangaroo Soft Toy", 'Toys', '99.99'),
(57, '333', 'Japan', '2020-10-13', 'Signed BTS Poster by BTS Jimin', 'Entertainment', '1310.95');

-- --------------------------------------------------------

--
-- Table structure for table `registered_users`
--

DROP TABLE IF EXISTS `registered_users`;
CREATE TABLE IF NOT EXISTS `registered_users` (
  `po_id` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `requester_id` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `paid_status` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
