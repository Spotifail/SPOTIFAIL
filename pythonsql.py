# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 17:17:16 2024

@author: angeladossantosribei
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 17:17:16 2024

@author: angeladossantosribei
"""

import sqlite3

conn = sqlite3.connect('spotify3.db')
cursor = conn.cursor()

script_sql = '''
CREATE TABLE IF NOT EXISTS `users` (
  `users_id` INTEGER PRIMARY KEY,
  `users_name` TEXT,
  `mot_de_passe` TEXT,
  `email` TEXT
);

CREATE TABLE IF NOT EXISTS `song` (
  `song_id` INTEGER PRIMARY KEY,
  `title` TEXT,
  `artist` TEXT,
  `duration` TEXT
);

CREATE TABLE IF NOT EXISTS `playlist` (
  `playlist_id` INTEGER PRIMARY KEY,
  `title_playlist` TEXT,
  `users_id` INTEGER,
  FOREIGN KEY (`users_id`) REFERENCES `users` (`users_id`)
);

CREATE TABLE IF NOT EXISTS `playlist_song` (
  `playlist_id` INTEGER,
  `song_id` INTEGER,
  `order` INTEGER,
  PRIMARY KEY (`playlist_id`, `song_id`),
  FOREIGN KEY (`playlist_id`) REFERENCES `playlist` (`playlist_id`),
  FOREIGN KEY (`song_id`) REFERENCES `song` (`song_id`)
);

CREATE TABLE IF NOT EXISTS `favorite` (
  `favorite_id` INTEGER PRIMARY KEY,
  `users_id` INTEGER,
  `song_id` INTEGER,
  FOREIGN KEY (`users_id`) REFERENCES `users` (`users_id`),
  FOREIGN KEY (`song_id`) REFERENCES `song` (`song_id`)
);

INSERT INTO `song` (`song_id`, `title`, `artist`, `duration`) 
VALUES (1, 'The Hill', 'The Weeknd', '3:55');
INSERT INTO `song` (`song_id`, `title`, `artist`, `duration`) 
VALUES (2, 'Save your tears', 'The Weeknd', '4:09');
INSERT INTO `song` (`song_id`, `title`, `artist`, `duration`) 
VALUES (3, 'Blinding lights', 'The Weeknd', '4:23');


INSERT INTO `playlist_song` (`playlist_id`, `song_id`, `order`) 
VALUES (1, 1, 1);  
INSERT INTO `playlist_song` (`playlist_id`, `song_id`, `order`) 
VALUES (1, 2, 2);
INSERT INTO `playlist_song` (`playlist_id`, `song_id`, `order`) 
VALUES (1, 3, 3);  

INSERT INTO 'users'('users_id','users_name')
VALUES(1,'anonyme');
'''

cursor.executescript(script_sql)

conn.commit()
conn.close()
