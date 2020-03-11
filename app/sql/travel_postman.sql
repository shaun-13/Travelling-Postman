-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 06, 2020 at 05:27 PM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

DROP DATABASE IF EXISTS travel_postman;

CREATE DATABASE travel_postman;
USE travel_postman;
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `travel_postman`
--

-- --------------------------------------------------------

--
-- Table structure for table `preorder`
--

DROP TABLE IF EXISTS `preorder`;
CREATE TABLE IF NOT EXISTS `preorder` (
  `poid` varchar(10) CHARACTER SET utf8 NOT NULL,
  `travellerid` varchar(10) CHARACTER SET utf8 NOT NULL,
  `country` varchar(80) CHARACTER SET utf8 NOT NULL,
  `end date` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `item name` varchar(80) CHARACTER SET utf8 NOT NULL,
  `item category` varchar(80) CHARACTER SET utf8 NOT NULL,
  `price` decimal(8,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `registered_po`
--

DROP TABLE IF EXISTS `registered`;
CREATE TABLE IF NOT EXISTS `registered` (
  `poid` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `requester id` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `paid status` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `userid` varchar(30) CHARACTER SET utf8 DEFAULT NULL,
  `name` varchar(80) CHARACTER SET utf8 DEFAULT NULL,
  `travellerid` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `requesterid` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `password` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `email` varchar(30) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userid`, `name`, `travellerid`, `requesterid`, `password`, `email`) VALUES
('100', 'Mister Postman', '200', '300', '123', 'postman@email.com');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
