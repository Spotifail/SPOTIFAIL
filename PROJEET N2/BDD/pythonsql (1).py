# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 17:17:16 2024

@author: angeladossantosribei
"""

import sqlite3

conn = sqlite3.connect('ma_base_de_donnees.db')
cursor = conn.cursor()

script_sql = '''
CREATE TABLE `users` (
  `users_id` INTEGER PRIMARY KEY,
  `users_name` TEXT,
  `mot_de_passe` TEXT,
  `email` TEXT
);

CREATE TABLE `song` (
  `song_id` INTEGER PRIMARY KEY,
  `title` TEXT,
  `artist` TEXT,
  `duration` TIMESTAMP
);

CREATE TABLE `playlist` (
  `playlist_id` INTEGER PRIMARY KEY,
  `title_playlist` TEXT,
  `users_id` INTEGER,
  FOREIGN KEY (`users_id`) REFERENCES `users` (`users_id`)
);

CREATE TABLE `playlist_song` (
  `playlist_id` INTEGER,
  `song_id` INTEGER,
  `order` INTEGER,
  PRIMARY KEY (`playlist_id`, `song_id`),
  FOREIGN KEY (`playlist_id`) REFERENCES `playlist` (`playlist_id`),
  FOREIGN KEY (`song_id`) REFERENCES `song` (`song_id`)
);

CREATE TABLE `favorite` (
  `favorite_id` INTEGER PRIMARY KEY,
  `users_id` INTEGER,
  `song_id` INTEGER,
  FOREIGN KEY (`users_id`) REFERENCES `users` (`users_id`),
  FOREIGN KEY (`song_id`) REFERENCES `song` (`song_id`)
);
'''

cursor.executescript(script_sql)

conn.commit()
conn.close()
