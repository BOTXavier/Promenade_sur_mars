-- phpMyAdmin SQL Dump
-- version 5.1.4deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 09, 2023 at 02:12 PM
-- Server version: 8.0.32-0ubuntu0.22.10.2
-- PHP Version: 8.1.7-1ubuntu3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Promanade_Sur_Mars`
--

-- --------------------------------------------------------

--
-- Table structure for table `identification`
--

CREATE TABLE `identification` (
  `idUser` int NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `login` varchar(100) NOT NULL,
  `motPasse` varchar(100) NOT NULL,
  `statut` int NOT NULL DEFAULT '1',
  `avatar` varchar(20) NOT NULL DEFAULT '1.png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Photos`
--

CREATE TABLE `Photos` (
  `id_photo` int NOT NULL,
  `sol` int NOT NULL,
  `rover` int NOT NULL,
  `camera` int NOT NULL,
  `url` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

------------------------------------------------------------

-- Tables pour la gestion des photos

CREATE TABLE `Photos` (
  `photo_id` int NOT NULL,
  `sol` int,
  `rover_id` int NOT NULL,
  `camera_id` int NOT NULL,
  `url` text NOT NULL,
  PRIMARY KEY(photo_id),
  FOREIGN KEY(rover_id) REFERENCES Rovers(rover_id) ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY(camera_id) REFERENCES Cameras(camera_id)ON DELETE SET NULL ON UPDATE CASCADE,
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Rovers` (
  `rover_id` int NOT NULL,
  `name` text NOT NULL,
  `landing_date` datetime,
  `launch_date` datetime,
  `status` text NOT NULL,
  PRIMARY KEY(rover_id),
  FOREIGN KEY(photo_id) REFERENCES Photos(photo_id) ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY(camera_id) REFERENCES Cameras(camera_id)ON DELETE SET NULL ON UPDATE CASCADE,
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Cameras` (
  `camera_id` int NOT NULL,
  `name` text NOT NULL,
  `rover_id` int NOT NULL,
  `full_name` text NOT NULL,
  PRIMARY KEY(camera_id),
  FOREIGN KEY(photo_id) REFERENCES Photos(photo_id)ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY(rover_id) REFERENCES Rovers(rover_id) ON DELETE SET NULL ON UPDATE CASCADE,
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Positions` (
  `posi_id` int NOT NULL,
  'rover_id' int NOT NULL,
  `lat` float,
  `long` float,
  `cap` float,
  PRIMARY KEY(posi_id),
  FOREIGN KEY(rover_id) REFERENCES Rovers(rover_id) ON DELETE SET NULL ON UPDATE CASCADE,
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

------------------------------------------------------------





--
-- Indexes for dumped tables
--

--
-- Indexes for table `identification`
--
ALTER TABLE `identification`
  ADD PRIMARY KEY (`idUser`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `identification`
--
ALTER TABLE `identification`
  MODIFY `idUser` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
