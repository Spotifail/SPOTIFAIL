CREATE TABLE `users` (
  `users_id` integer PRIMARY KEY,
  `users_name` varchar(255),
  `mot_de_passe` varchar(255),
  `email` varchar(255)
);

CREATE TABLE `song` (
  `song_id` integer PRIMARY KEY,
  `title` varchar(255),
  `artist` varchar(255),
  `duration` timestamp
);

CREATE TABLE `playlist` (
  `playist_id` integer PRIMARY KEY,
  `title_playlist` varchar(255),
  `users_id` integer
);

CREATE TABLE `playlist_song` (
  `playist_id` integer PRIMARY KEY,
  `song_id` integer,
  `order` integer
);

CREATE TABLE `favorite` (
  `favorite_id` integer PRIMARY KEY,
  `users_id` integer,
  `song_id` integer
);

ALTER TABLE `favorite` ADD FOREIGN KEY (`users_id`) REFERENCES `users` (`users_id`);

ALTER TABLE `users` ADD FOREIGN KEY (`users_id`) REFERENCES `playlist` (`users_id`);

ALTER TABLE `playlist_song` ADD FOREIGN KEY (`song_id`) REFERENCES `song` (`song_id`);

ALTER TABLE `song` ADD FOREIGN KEY (`song_id`) REFERENCES `favorite` (`song_id`);

ALTER TABLE `playlist_song` ADD FOREIGN KEY (`playist_id`) REFERENCES `playlist` (`playist_id`);
