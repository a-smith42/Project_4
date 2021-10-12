CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(255),
  `fName` varchar(255),
  `sName` varchar(255),
  `email` varchar(255)
);

CREATE TABLE `tracks` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255),
  `length` float,
  `artistID` int,
  `albumID` int
);

CREATE TABLE `artists` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

CREATE TABLE `albums` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

CREATE TABLE `genres` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

CREATE TABLE `track_genres` (
  `genreID` int,
  `trackID` int
);

CREATE TABLE `playlist` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `userID` int,
  `title` varchar(255),
  `length` float
);

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
