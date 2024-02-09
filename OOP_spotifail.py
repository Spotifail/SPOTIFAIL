import sqlite3

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def display_info(self):
        print(f"Title: {self.title}\nArtist: {self.artist}\nDuration: {self.duration} seconds")

class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        # Additional: Add the song to the database
        self._add_song_to_database(song)

    def _add_song_to_database(self, song):
        # SQLite code to insert the song into the database
        conn = sqlite3.connect("music_database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO songs (title, artist, duration) VALUES (?, ?, ?)",
                       (song.title, song.artist, song.duration))
        conn.commit()
        conn.close()

# Example usage:
song1 = Song("Song Title 1", "Artist 1", 180)
playlist1 = Playlist("My Playlist")
playlist1.add_song(song1)
