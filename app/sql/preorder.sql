-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 22, 2020 at 04:04 PM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

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
  `po_id` int(10) NOT NULL,
  `traveller_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `country` varchar(80) CHARACTER SET utf8 NOT NULL,
  `end_date` date NOT NULL,
  `item_name` varchar(30) CHARACTER SET utf8 NOT NULL,
  `item_category` varchar(30) CHARACTER SET utf8 NOT NULL,
  `price` decimal(8,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `preorder_details`
--

INSERT INTO `preorder_details` (`po_id`, `traveller_id`, `country`, `end_date`, `item_name`, `item_category`, `price`) VALUES
(1, '333', 'Iceland', '2019-01-01', 'chinese bowl', 'food', '23.20');

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
