DROP DATABASE IF EXISTS project_4;
CREATE DATABASE IF NOT EXISTS project_4;
USE project_4;

/*users signed in through app*/
DROP TABLE IF EXISTS users;
CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(255),
  `fName` varchar(255),
  `sName` varchar(255),
  `email` varchar(255)
  /*authenticated boolean - ???*/
);

/*to pull from spotify*/
DROP TABLE IF EXISTS tracks;
CREATE TABLE `tracks` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255),
  `length` float,
  `artistID` int,
  `albumID` int
);

/*to pull from spotify*/
DROP TABLE IF EXISTS artists;
CREATE TABLE `artists` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

/*to pull from spotify*/
DROP TABLE IF EXISTS albums;
CREATE TABLE `albums` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

/*to pull from spotify*/
DROP TABLE IF EXISTS genres;
CREATE TABLE `genres` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

/*to pull from spotify*/
DROP TABLE IF EXISTS tracks_genres;
CREATE TABLE `track_genres` (
  `genreID` int,
  `trackID` int
);

DROP TABLE IF EXISTS playlist;
CREATE TABLE `playlist` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `userID` int,
  `title` varchar(255),
  `length` float
);

DROP TABLE IF EXISTS playlist_tracks;
CREATE TABLE `playlist_tracks` (
  `playlistID` int,
  `trackID` int
);

ALTER TABLE `tracks` ADD FOREIGN KEY (`artistID`) REFERENCES `artists` (`id`);

ALTER TABLE `tracks` ADD FOREIGN KEY (`albumID`) REFERENCES `albums` (`id`);

ALTER TABLE `track_genres` ADD FOREIGN KEY (`genreID`) REFERENCES `genres` (`id`);

ALTER TABLE `track_genres` ADD FOREIGN KEY (`trackID`) REFERENCES `tracks` (`id`);

ALTER TABLE `playlist` ADD FOREIGN KEY (`userID`) REFERENCES `users` (`id`);

ALTER TABLE `playlist_tracks` ADD FOREIGN KEY (`playlistID`) REFERENCES `playlist` (`id`);

ALTER TABLE `playlist_tracks` ADD FOREIGN KEY (`trackID`) REFERENCES `tracks` (`id`);

