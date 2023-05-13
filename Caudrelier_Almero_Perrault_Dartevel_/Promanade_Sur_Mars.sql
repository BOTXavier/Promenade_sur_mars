-- phpMyAdmin SQL Dump
-- version 5.1.4deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 13, 2023 at 06:30 PM
-- Server version: 8.0.33-0ubuntu0.22.10.1
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
-- Table structure for table `Camera`
--

CREATE TABLE `Camera` (
  `id_camera` int NOT NULL,
  `name` text NOT NULL,
  `full_name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Photos`
--

INSERT INTO `Photos` (`id_photo`, `sol`, `rover`, `camera`, `url`) VALUES
(287319, 1, 7, 27, 'http://mars.nasa.gov/mer/gallery/all/2/f/001/2F126468064EDN0000P1001L0M1-BR.JPG'),
(287320, 1, 7, 27, 'http://mars.nasa.gov/mer/gallery/all/2/f/001/2F126468064EDN0000P1001R0M1-BR.JPG'),
(290673, 1, 7, 28, 'http://mars.nasa.gov/mer/gallery/all/2/r/001/2R126468012EDN0000P1002L0M1-BR.JPG'),
(290674, 1, 7, 28, 'http://mars.nasa.gov/mer/gallery/all/2/r/001/2R126468012EDN0000P1002R0M1-BR.JPG'),
(318416, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126467960EDN0000P1500L0M1-BR.JPG'),
(318417, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126467960EDN0000P1500R0M1-BR.JPG'),
(318418, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468200EDN0000P1502L0M1-BR.JPG'),
(318419, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468200EDN0000P1502R0M1-BR.JPG'),
(318420, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468253EDN0000P1502L0M1-BR.JPG'),
(318421, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468253EDN0000P1502R0M1-BR.JPG'),
(318422, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468305EDN0000P1502L0M1-BR.JPG'),
(318423, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468305EDN0000P1502R0M1-BR.JPG'),
(318424, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468357EDN0000P1502L0M1-BR.JPG'),
(318425, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468357EDN0000P1502R0M1-BR.JPG'),
(318426, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468424EDN0000P1502L0M1-BR.JPG'),
(318427, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468424EDN0000P1502R0M1-BR.JPG'),
(318428, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468476EDN0000P1502L0M1-BR.JPG'),
(318429, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468476EDN0000P1502R0M1-BR.JPG'),
(318430, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468527EDN0000P1502L0M1-BR.JPG'),
(318431, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468527EDN0000P1502R0M1-BR.JPG'),
(318432, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468579EDN0000P1502L0M1-BR.JPG'),
(318433, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468579EDN0000P1502R0M1-BR.JPG'),
(318434, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468631EDN0000P1502L0M1-BR.JPG'),
(318435, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468631EDN0000P1502R0M1-BR.JPG'),
(318436, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468719EDN0000P1502L0M1-BR.JPG'),
(318437, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468719EDN0000P1502R0M1-BR.JPG'),
(318438, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468852EDN0000P1503L0M1-BR.JPG'),
(318439, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468852EDN0000P1503R0M1-BR.JPG'),
(318440, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468889EDN0000P1503L0M1-BR.JPG'),
(318441, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468889EDN0000P1503R0M1-BR.JPG'),
(318442, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468921EDN0000P1503L0M1-BR.JPG'),
(318443, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468921EDN0000P1503R0M1-BR.JPG'),
(318444, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468972EDN0000P1503L0M1-BR.JPG'),
(318445, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468972EDN0000P1503R0M1-BR.JPG'),
(318446, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469021EDN0000P1503L0M1-BR.JPG'),
(318447, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469021EDN0000P1503R0M1-BR.JPG'),
(318448, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469072EDN0000P1503L0M1-BR.JPG'),
(318449, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469072EDN0000P1503R0M1-BR.JPG'),
(318450, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469104EDN0000P1503L0M1-BR.JPG'),
(318451, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469104EDN0000P1503R0M1-BR.JPG'),
(318452, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469170EDN0000P1503L0M1-BR.JPG'),
(318453, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469170EDN0000P1503R0M1-BR.JPG'),
(318454, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469222EDN0000P1503L0M1-BR.JPG'),
(318455, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469222EDN0000P1503R0M1-BR.JPG'),
(318456, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469273EDN0000P1503L0M1-BR.JPG'),
(318457, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469273EDN0000P1503R0M1-BR.JPG'),
(318458, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469324EDN0000P1503L0M1-BR.JPG'),
(318459, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469324EDN0000P1503R0M1-BR.JPG'),
(318460, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469375EDN0000P1503L0M1-BR.JPG'),
(318461, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469375EDN0000P1503R0M1-BR.JPG'),
(318462, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469447EDN0000P1503L0M1-BR.JPG'),
(318463, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469447EDN0000P1503R0M1-BR.JPG'),
(318464, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469500EDN0000P1501L0M1-BR.JPG'),
(318465, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469500EDN0000P1501R0M1-BR.JPG'),
(318466, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469557EDN0000P1501L0M1-BR.JPG'),
(318467, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469557EDN0000P1501R0M1-BR.JPG'),
(318468, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469615EDN0000P1501L0M1-BR.JPG'),
(318469, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469615EDN0000P1501R0M1-BR.JPG'),
(318470, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469670EDN0000P1501L0M1-BR.JPG'),
(318471, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469670EDN0000P1501R0M1-BR.JPG'),
(318472, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469721EDN0000P1501L0M1-BR.JPG'),
(318473, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469721EDN0000P1501R0M1-BR.JPG'),
(318474, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469774EDN0000P1501L0M1-BR.JPG'),
(318475, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469774EDN0000P1501R0M1-BR.JPG'),
(318476, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468796ESF0000P1531L0M1-BR.JPG'),
(397363, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471307EFF0000P2303L2M1-BR.JPG'),
(397364, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471391EFF0000P2303L2M1-BR.JPG'),
(397365, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471476EFF0000P2303L2M1-BR.JPG'),
(397366, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471340EDN0000P2303L5M1-BR.JPG'),
(397367, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471364EDN0000P2303L6M1-BR.JPG'),
(397368, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471425EDN0000P2303L5M1-BR.JPG'),
(397369, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471450EDN0000P2303L6M1-BR.JPG'),
(397370, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471510EDN0000P2303L5M1-BR.JPG'),
(397371, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471535EDN0000P2303L6M1-BR.JPG'),
(403583, 1, 7, 32, 'http://mars.nasa.gov/mer/gallery/all/2/e/001/2E126462398EDN0000F0006N0M1-BR.JPG'),
(403584, 1, 7, 32, 'http://mars.nasa.gov/mer/gallery/all/2/e/001/2E126462401EDN0000F0006N0M1-BR.JPG'),
(403585, 1, 7, 32, 'http://mars.nasa.gov/mer/gallery/all/2/e/001/2E126462405EDN0000F0006N0M1-BR.JPG'),
(287319, 1, 7, 27, 'http://mars.nasa.gov/mer/gallery/all/2/f/001/2F126468064EDN0000P1001L0M1-BR.JPG'),
(287320, 1, 7, 27, 'http://mars.nasa.gov/mer/gallery/all/2/f/001/2F126468064EDN0000P1001R0M1-BR.JPG'),
(290673, 1, 7, 28, 'http://mars.nasa.gov/mer/gallery/all/2/r/001/2R126468012EDN0000P1002L0M1-BR.JPG'),
(290674, 1, 7, 28, 'http://mars.nasa.gov/mer/gallery/all/2/r/001/2R126468012EDN0000P1002R0M1-BR.JPG'),
(318416, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126467960EDN0000P1500L0M1-BR.JPG'),
(318417, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126467960EDN0000P1500R0M1-BR.JPG'),
(318418, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468200EDN0000P1502L0M1-BR.JPG'),
(318419, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468200EDN0000P1502R0M1-BR.JPG'),
(318420, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468253EDN0000P1502L0M1-BR.JPG'),
(318421, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468253EDN0000P1502R0M1-BR.JPG'),
(318422, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468305EDN0000P1502L0M1-BR.JPG'),
(318423, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468305EDN0000P1502R0M1-BR.JPG'),
(318424, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468357EDN0000P1502L0M1-BR.JPG'),
(318425, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468357EDN0000P1502R0M1-BR.JPG'),
(318426, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468424EDN0000P1502L0M1-BR.JPG'),
(318427, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468424EDN0000P1502R0M1-BR.JPG'),
(318428, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468476EDN0000P1502L0M1-BR.JPG'),
(318429, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468476EDN0000P1502R0M1-BR.JPG'),
(318430, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468527EDN0000P1502L0M1-BR.JPG'),
(318431, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468527EDN0000P1502R0M1-BR.JPG'),
(318432, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468579EDN0000P1502L0M1-BR.JPG'),
(318433, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468579EDN0000P1502R0M1-BR.JPG'),
(318434, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468631EDN0000P1502L0M1-BR.JPG'),
(318435, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468631EDN0000P1502R0M1-BR.JPG'),
(318436, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468719EDN0000P1502L0M1-BR.JPG'),
(318437, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468719EDN0000P1502R0M1-BR.JPG'),
(318438, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468852EDN0000P1503L0M1-BR.JPG'),
(318439, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468852EDN0000P1503R0M1-BR.JPG'),
(318440, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468889EDN0000P1503L0M1-BR.JPG'),
(318441, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468889EDN0000P1503R0M1-BR.JPG'),
(318442, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468921EDN0000P1503L0M1-BR.JPG'),
(318443, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468921EDN0000P1503R0M1-BR.JPG'),
(318444, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468972EDN0000P1503L0M1-BR.JPG'),
(318445, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468972EDN0000P1503R0M1-BR.JPG'),
(318446, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469021EDN0000P1503L0M1-BR.JPG'),
(318447, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469021EDN0000P1503R0M1-BR.JPG'),
(318448, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469072EDN0000P1503L0M1-BR.JPG'),
(318449, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469072EDN0000P1503R0M1-BR.JPG'),
(318450, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469104EDN0000P1503L0M1-BR.JPG'),
(318451, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469104EDN0000P1503R0M1-BR.JPG'),
(318452, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469170EDN0000P1503L0M1-BR.JPG'),
(318453, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469170EDN0000P1503R0M1-BR.JPG'),
(318454, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469222EDN0000P1503L0M1-BR.JPG'),
(318455, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469222EDN0000P1503R0M1-BR.JPG'),
(318456, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469273EDN0000P1503L0M1-BR.JPG'),
(318457, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469273EDN0000P1503R0M1-BR.JPG'),
(318458, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469324EDN0000P1503L0M1-BR.JPG'),
(318459, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469324EDN0000P1503R0M1-BR.JPG'),
(318460, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469375EDN0000P1503L0M1-BR.JPG'),
(318461, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469375EDN0000P1503R0M1-BR.JPG'),
(318462, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469447EDN0000P1503L0M1-BR.JPG'),
(318463, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469447EDN0000P1503R0M1-BR.JPG'),
(318464, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469500EDN0000P1501L0M1-BR.JPG'),
(318465, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469500EDN0000P1501R0M1-BR.JPG'),
(318466, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469557EDN0000P1501L0M1-BR.JPG'),
(318467, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469557EDN0000P1501R0M1-BR.JPG'),
(318468, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469615EDN0000P1501L0M1-BR.JPG'),
(318469, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469615EDN0000P1501R0M1-BR.JPG'),
(318470, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469670EDN0000P1501L0M1-BR.JPG'),
(318471, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469670EDN0000P1501R0M1-BR.JPG'),
(318472, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469721EDN0000P1501L0M1-BR.JPG'),
(318473, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469721EDN0000P1501R0M1-BR.JPG'),
(318474, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469774EDN0000P1501L0M1-BR.JPG'),
(318475, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469774EDN0000P1501R0M1-BR.JPG'),
(318476, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468796ESF0000P1531L0M1-BR.JPG'),
(397363, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471307EFF0000P2303L2M1-BR.JPG'),
(397364, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471391EFF0000P2303L2M1-BR.JPG'),
(397365, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471476EFF0000P2303L2M1-BR.JPG'),
(397366, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471340EDN0000P2303L5M1-BR.JPG'),
(397367, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471364EDN0000P2303L6M1-BR.JPG'),
(397368, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471425EDN0000P2303L5M1-BR.JPG'),
(397369, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471450EDN0000P2303L6M1-BR.JPG'),
(397370, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471510EDN0000P2303L5M1-BR.JPG'),
(397371, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471535EDN0000P2303L6M1-BR.JPG'),
(403583, 1, 7, 32, 'http://mars.nasa.gov/mer/gallery/all/2/e/001/2E126462398EDN0000F0006N0M1-BR.JPG'),
(403584, 1, 7, 32, 'http://mars.nasa.gov/mer/gallery/all/2/e/001/2E126462401EDN0000F0006N0M1-BR.JPG'),
(403585, 1, 7, 32, 'http://mars.nasa.gov/mer/gallery/all/2/e/001/2E126462405EDN0000F0006N0M1-BR.JPG'),
(287319, 1, 7, 27, 'http://mars.nasa.gov/mer/gallery/all/2/f/001/2F126468064EDN0000P1001L0M1-BR.JPG'),
(287320, 1, 7, 27, 'http://mars.nasa.gov/mer/gallery/all/2/f/001/2F126468064EDN0000P1001R0M1-BR.JPG'),
(290673, 1, 7, 28, 'http://mars.nasa.gov/mer/gallery/all/2/r/001/2R126468012EDN0000P1002L0M1-BR.JPG'),
(290674, 1, 7, 28, 'http://mars.nasa.gov/mer/gallery/all/2/r/001/2R126468012EDN0000P1002R0M1-BR.JPG'),
(318416, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126467960EDN0000P1500L0M1-BR.JPG'),
(318417, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126467960EDN0000P1500R0M1-BR.JPG'),
(318418, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468200EDN0000P1502L0M1-BR.JPG'),
(318419, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468200EDN0000P1502R0M1-BR.JPG'),
(318420, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468253EDN0000P1502L0M1-BR.JPG'),
(318421, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468253EDN0000P1502R0M1-BR.JPG'),
(318422, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468305EDN0000P1502L0M1-BR.JPG'),
(318423, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468305EDN0000P1502R0M1-BR.JPG'),
(318424, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468357EDN0000P1502L0M1-BR.JPG'),
(318425, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468357EDN0000P1502R0M1-BR.JPG'),
(318426, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468424EDN0000P1502L0M1-BR.JPG'),
(318427, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468424EDN0000P1502R0M1-BR.JPG'),
(318428, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468476EDN0000P1502L0M1-BR.JPG'),
(318429, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468476EDN0000P1502R0M1-BR.JPG'),
(318430, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468527EDN0000P1502L0M1-BR.JPG'),
(318431, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468527EDN0000P1502R0M1-BR.JPG'),
(318432, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468579EDN0000P1502L0M1-BR.JPG'),
(318433, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468579EDN0000P1502R0M1-BR.JPG'),
(318434, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468631EDN0000P1502L0M1-BR.JPG'),
(318435, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468631EDN0000P1502R0M1-BR.JPG'),
(318436, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468719EDN0000P1502L0M1-BR.JPG'),
(318437, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468719EDN0000P1502R0M1-BR.JPG'),
(318438, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468852EDN0000P1503L0M1-BR.JPG'),
(318439, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468852EDN0000P1503R0M1-BR.JPG'),
(318440, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468889EDN0000P1503L0M1-BR.JPG'),
(318441, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468889EDN0000P1503R0M1-BR.JPG'),
(318442, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468921EDN0000P1503L0M1-BR.JPG'),
(318443, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468921EDN0000P1503R0M1-BR.JPG'),
(318444, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468972EDN0000P1503L0M1-BR.JPG'),
(318445, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468972EDN0000P1503R0M1-BR.JPG'),
(318446, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469021EDN0000P1503L0M1-BR.JPG'),
(318447, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469021EDN0000P1503R0M1-BR.JPG'),
(318448, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469072EDN0000P1503L0M1-BR.JPG'),
(318449, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469072EDN0000P1503R0M1-BR.JPG'),
(318450, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469104EDN0000P1503L0M1-BR.JPG'),
(318451, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469104EDN0000P1503R0M1-BR.JPG'),
(318452, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469170EDN0000P1503L0M1-BR.JPG'),
(318453, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469170EDN0000P1503R0M1-BR.JPG'),
(318454, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469222EDN0000P1503L0M1-BR.JPG'),
(318455, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469222EDN0000P1503R0M1-BR.JPG'),
(318456, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469273EDN0000P1503L0M1-BR.JPG'),
(318457, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469273EDN0000P1503R0M1-BR.JPG'),
(318458, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469324EDN0000P1503L0M1-BR.JPG'),
(318459, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469324EDN0000P1503R0M1-BR.JPG'),
(318460, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469375EDN0000P1503L0M1-BR.JPG'),
(318461, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469375EDN0000P1503R0M1-BR.JPG'),
(318462, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469447EDN0000P1503L0M1-BR.JPG'),
(318463, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469447EDN0000P1503R0M1-BR.JPG'),
(318464, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469500EDN0000P1501L0M1-BR.JPG'),
(318465, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469500EDN0000P1501R0M1-BR.JPG'),
(318466, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469557EDN0000P1501L0M1-BR.JPG'),
(318467, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469557EDN0000P1501R0M1-BR.JPG'),
(318468, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469615EDN0000P1501L0M1-BR.JPG'),
(318469, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469615EDN0000P1501R0M1-BR.JPG'),
(318470, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469670EDN0000P1501L0M1-BR.JPG'),
(318471, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469670EDN0000P1501R0M1-BR.JPG'),
(318472, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469721EDN0000P1501L0M1-BR.JPG'),
(318473, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469721EDN0000P1501R0M1-BR.JPG'),
(318474, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469774EDN0000P1501L0M1-BR.JPG'),
(318475, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126469774EDN0000P1501R0M1-BR.JPG'),
(318476, 1, 7, 29, 'http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126468796ESF0000P1531L0M1-BR.JPG'),
(397363, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471307EFF0000P2303L2M1-BR.JPG'),
(397364, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471391EFF0000P2303L2M1-BR.JPG'),
(397365, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471476EFF0000P2303L2M1-BR.JPG'),
(397366, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471340EDN0000P2303L5M1-BR.JPG'),
(397367, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471364EDN0000P2303L6M1-BR.JPG'),
(397368, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471425EDN0000P2303L5M1-BR.JPG'),
(397369, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471450EDN0000P2303L6M1-BR.JPG'),
(397370, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471510EDN0000P2303L5M1-BR.JPG'),
(397371, 1, 7, 30, 'http://mars.nasa.gov/mer/gallery/all/2/p/001/2P126471535EDN0000P2303L6M1-BR.JPG'),
(403583, 1, 7, 32, 'http://mars.nasa.gov/mer/gallery/all/2/e/001/2E126462398EDN0000F0006N0M1-BR.JPG'),
(403584, 1, 7, 32, 'http://mars.nasa.gov/mer/gallery/all/2/e/001/2E126462401EDN0000F0006N0M1-BR.JPG'),
(403585, 1, 7, 32, 'http://mars.nasa.gov/mer/gallery/all/2/e/001/2E126462405EDN0000F0006N0M1-BR.JPG');

-- --------------------------------------------------------

--
-- Table structure for table `Rover`
--

CREATE TABLE `Rover` (
  `id_Rover` int NOT NULL,
  `name` text NOT NULL,
  `landing_date` date NOT NULL,
  `launch_date` date NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
