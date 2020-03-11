DROP DATABASE IF EXISTS preorder;
CREATE DATABASE IF NOT EXISTS preorder;
USE preorder;

-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 11, 2020 at 12:27 PM
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
-- Database: preorder
--
-- --------------------------------------------------------

--
-- Table structure for table preorder_details
--

DROP TABLE IF EXISTS preorder_details;
CREATE TABLE IF NOT EXISTS preorder_details (
  po_id int(10) NOT NULL AUTO_INCREMENT,
  traveller_id int(32) NOT NULL,
  country text NOT NULL,
  end_date date NOT NULL,
  item_name varchar(32) NOT NULL,
  item_category varchar(32) NOT NULL,
  price decimal(8,2) NOT NULL,
  CONSTRAINT preorder_details_pk PRIMARY KEY (po_id)

) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table preorder_details
--

INSERT INTO preorder_details (po_id, traveller_id, country, end_date, item_name, item_category, price) VALUES
(1234, 1111111111, 'Singapore', '2020-03-31', 'Witch Broom', 'Witch Crafts', '99.30'),
(1235, 1111111112, 'Malaysia', '2020-03-27', 'Angsty', 'Cakes', '7.23');

-- --------------------------------------------------------

--
-- Table structure for table registered_users
--

DROP TABLE IF EXISTS registered_users;
CREATE TABLE IF NOT EXISTS registered_users (
  po_id int(10) NOT NULL,
  requester_id int(32) NOT NULL,
  CONSTRAINT registered_users_pk PRIMARY KEY (po_id,requester_id),
  CONSTRAINT registered_users_fk FOREIGN KEY (po_id) REFERENCES preorder_details(po_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
