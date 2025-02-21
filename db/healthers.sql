-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 21, 2025 at 09:57 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `healthers`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userID` int(11) NOT NULL,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL DEFAULT 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userID`, `firstName`, `lastName`, `email`, `password`, `role`) VALUES
(1, 'asd', 'dsa', 'asd@gmail.com', 'pbkdf2:sha256:600000$V50DB5SbxifGdpoB$206ddefbf753b88fe603a608d40393378f94a17854b0e5406668e657da6d95f1', 'user'),
(9, 'joji', 'vlogs', 'joji@gmail.com', 'pbkdf2:sha256:600000$970wPe8T395xJVq5$0b9d240fad46ce2cc15e106c6a54ac29bf15e79ac561dceba21553fcf4fe606f', 'user'),
(10, 'joji', 'vlogs', 'vlog@gmail.com', 'pbkdf2:sha256:600000$bkJAcTieVbtzS1iI$359564be5701ee0325576ec6392333e3090368d86e58aa1cf235ba59e69dc63c', 'user'),
(12, 's21', 'test', 's21contactemail@gmail.com', 'pbkdf2:sha256:1000000$9QNoxpHnbuPl5szV$06fa9b647edf6a256cb526f56d4cf9fe84bf3e9d5d7c13fa3315150a3087dce5', 'user');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userID`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
