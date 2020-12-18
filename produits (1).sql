-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 18 déc. 2020 à 13:13
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
-- Base de données : `produits`
--

-- --------------------------------------------------------

--
-- Structure de la table `produits`
--

DROP TABLE IF EXISTS `produits`;
CREATE TABLE IF NOT EXISTS `produits` (
  `id_product_google` int(11) NOT NULL,
  `price` float(10,0) NOT NULL,
  `date_creation` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_update` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `id_product` varchar(30) NOT NULL,
  `reference` varchar(20) NOT NULL,
  `numero` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`numero`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `produits`
--

INSERT INTO `produits` (`id_product_google`, `price`, `date_creation`, `date_update`, `id_product`, `reference`, `numero`) VALUES
(1, 52, '2020-12-16 20:40:45', '2020-12-16 20:40:45', '3', '1', 1),
(2, 21, '2020-12-17 08:24:11', '2020-12-17 08:24:11', '2', '2', 2),
(15, 46, '2020-12-17 08:44:42', '2020-12-17 08:44:42', '15', '3', 3),
(13, 43, '2020-12-17 16:43:34', '2020-12-17 16:43:34', '13', '12', 4),
(2, 78, '2020-12-17 11:44:11', '2020-12-18 11:44:37', '2', '2', 5),
(45, 175, '2020-12-18 12:38:41', '2020-12-18 12:38:41', '45', '78', 6),
(78, 78, '2020-12-18 13:18:55', '2020-12-18 13:18:55', '78', '78', 7),
(78, 78, '2020-12-18 13:18:55', '2020-12-18 13:18:55', '78', '78', 8);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
