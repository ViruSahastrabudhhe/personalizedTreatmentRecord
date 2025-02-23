-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 23, 2025 at 05:35 AM
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
-- Table structure for table `patientinfo`
--

CREATE TABLE `patientinfo` (
  `patientInfoID` bigint(20) NOT NULL,
  `userID` bigint(20) NOT NULL,
  `patientFname` varchar(255) DEFAULT NULL,
  `patientLname` varchar(255) DEFAULT NULL,
  `patientContactNo` varchar(255) DEFAULT NULL,
  `patientSex` varchar(255) DEFAULT NULL,
  `patientBirthday` date DEFAULT NULL,
  `patientProvince` varchar(255) DEFAULT NULL,
  `patientCity` varchar(255) DEFAULT NULL,
  `patientBarangay` varchar(255) DEFAULT NULL,
  `patientTown` varchar(255) DEFAULT NULL,
  `patientStreet` varchar(255) DEFAULT NULL,
  `patientDateRegistered` datetime DEFAULT NULL,
  `patientDateConsulted` datetime DEFAULT NULL,
  `patientDateUpdated` datetime NOT NULL,
  `isArchived` tinyint(4) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `patientmedicalinfo`
--

CREATE TABLE `patientmedicalinfo` (
  `medicalInfoID` bigint(20) NOT NULL,
  `userID` bigint(20) NOT NULL,
  `patientInfoID` bigint(20) NOT NULL,
  `diagnosis` varchar(255) NOT NULL,
  `findings` varchar(255) NOT NULL,
  `advice` varchar(255) DEFAULT NULL,
  `treatment` varchar(255) DEFAULT NULL,
  `evaluation` varchar(255) DEFAULT NULL,
  `medicalInfoDateCreated` datetime DEFAULT NULL,
  `medicalInfoDateUpdated` datetime DEFAULT NULL,
  `isArchived` tinyint(4) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `requests`
--

CREATE TABLE `requests` (
  `requestID` bigint(20) NOT NULL,
  `userID` bigint(20) NOT NULL,
  `applicantName` varchar(255) NOT NULL,
  `applicantContactNo` varchar(255) NOT NULL,
  `requestCategory` varchar(255) NOT NULL COMMENT 'nurse application/patient appointment',
  `requestType` varchar(255) NOT NULL COMMENT 'evaluation/advice/consultation/check up',
  `requestDateCreated` datetime NOT NULL,
  `requestDateUpdated` datetime NOT NULL,
  `requestDateArchived` datetime NOT NULL,
  `isArchived` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userID` bigint(20) NOT NULL,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL DEFAULT 'patient',
  `isArchived` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userID`, `firstName`, `lastName`, `email`, `password`, `role`, `isArchived`) VALUES
(12, 's21', 'test', 's21contactemail@gmail.com', 'pbkdf2:sha256:1000000$9QNoxpHnbuPl5szV$06fa9b647edf6a256cb526f56d4cf9fe84bf3e9d5d7c13fa3315150a3087dce5', 'nurse', 0),
(14, 'patient', 'test', 'patient@gmail.com', 'pbkdf2:sha256:1000000$8m34Ugd55y8493cW$fc784fe756865d173b6ef2b9514bdc451706d47d27af98d335eb62b7c78ba46c', 'patient', 0),
(16, 'admin', 'admin', 'admin@gmail.com', 'pbkdf2:sha256:1000000$XwwpESJ97R2mM9de$da06a90ae416e79f690446c6c897f6834625198505e2e190df336ba873d1d8a3', 'admin', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `patientinfo`
--
ALTER TABLE `patientinfo`
  ADD PRIMARY KEY (`patientInfoID`),
  ADD KEY `patientInfoUserID` (`userID`);

--
-- Indexes for table `patientmedicalinfo`
--
ALTER TABLE `patientmedicalinfo`
  ADD PRIMARY KEY (`medicalInfoID`),
  ADD KEY `medicalPatientInfoID` (`patientInfoID`),
  ADD KEY `patientMedicalInfoUserID` (`userID`);

--
-- Indexes for table `requests`
--
ALTER TABLE `requests`
  ADD PRIMARY KEY (`requestID`),
  ADD KEY `requestsUserID` (`userID`);

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
-- AUTO_INCREMENT for table `patientinfo`
--
ALTER TABLE `patientinfo`
  MODIFY `patientInfoID` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `patientmedicalinfo`
--
ALTER TABLE `patientmedicalinfo`
  MODIFY `medicalInfoID` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `requests`
--
ALTER TABLE `requests`
  MODIFY `requestID` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `userID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `patientinfo`
--
ALTER TABLE `patientinfo`
  ADD CONSTRAINT `patientInfoUserID` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`);

--
-- Constraints for table `patientmedicalinfo`
--
ALTER TABLE `patientmedicalinfo`
  ADD CONSTRAINT `medicalPatientInfoID` FOREIGN KEY (`patientInfoID`) REFERENCES `patientinfo` (`patientInfoID`),
  ADD CONSTRAINT `patientMedicalInfoUserID` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`);

--
-- Constraints for table `requests`
--
ALTER TABLE `requests`
  ADD CONSTRAINT `requestsUserID` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
