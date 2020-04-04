DROP DATABASE IF EXISTS user;
CREATE DATABASE IF NOT EXISTS user;
USE user;


-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 11, 2020 at 12:51 PM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: users
--

-- --------------------------------------------------------

--
-- Table structure for table user_details
--

DROP TABLE IF EXISTS user_details;
CREATE TABLE IF NOT EXISTS user_details (
  user_id varchar(100) NOT NULL,
  name varchar(100) NOT NULL,
  PRIMARY KEY (user_id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table user_details
--

-- INSERT INTO user_details (user_id, `name`) VALUES
-- (1111111111, 'Ahmad Sultiman'),
-- (1111111112, 'Rachel Bargaros');
-- COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
