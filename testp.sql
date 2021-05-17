-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 17 mai 2021 à 19:52
-- Version du serveur :  5.7.31
-- Version de PHP : 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `testjson`
--

-- --------------------------------------------------------

--
-- Structure de la table `testp`
--

DROP TABLE IF EXISTS `testp`;
CREATE TABLE IF NOT EXISTS `testp` (
  `date` varchar(255) NOT NULL,
  `nombreDeTest` varchar(255) NOT NULL,
  `positifs` varchar(255) NOT NULL,
  `tauxPositifs` varchar(255) NOT NULL,
  `cas_contact` varchar(255) NOT NULL,
  `cas_communautaire` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `testp`
--

INSERT INTO `testp` (`date`, `nombreDeTest`, `positifs`, `tauxPositifs`, `cas_contact`, `cas_communautaire`) VALUES
('Dimanche 20 décembre 2020', '1356', '88', '6,49', '29', '58'),
('Dimanche 21 mars 2021', '1894', '140', '7399', '44', '96'),
('Jeudi 1\"r avril 2021', '1659', '77', '4,64%', '17', '60'),
('Lundi 22 mars 2021', '1398', '87', '622%', '30', '57'),
('Mardi 09 mars 2021', '1028', '6', '778', '22', '58'),
('Mardi 23 mars 2021', '732', '36', '492%', '15', '21'),
('Samedi 19 décembre 2020', '1819', '111', '6,10', '43', '68'),
('Vendredi 18 décembre 2020', '1489', '108', '7,25', '47', '59');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
