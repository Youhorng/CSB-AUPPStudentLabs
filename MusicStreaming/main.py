import random
import csv
import os

class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length
    

class MusicLibrary:
    def __init__(self):
        
        with open('MusicStreaming/music.csv', 'r') as file:
            reader = csv.DictReader(file)
            self.song_list = list(reader)

    def add_song(self, song):
        if any(song_data["title"] == song.title and song_data["artist"] == song.artist for song_data in self.song_list):
            print("Song already exists")
            return 

        song_info = {
            "song_id": len(self.song_list) + 1, 
            "title": song.title,
            "artist": song.artist,
            "album": song.album,
            "genre": song.genre,
            "length": song.length
        }

        self.song_list.append(song_info)

        try: 
            with open('MusicStreaming/music.csv' ,'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=song_info.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(song_info)
        except FileNotFoundError:
            print("File not found")
            return

    def search_song(self):

        choice = input("------> Please enter choice you want to search by (title /artist /genre /album /length) : ").lower()

        if choice == "title":
            title = input("------> Please enter title: ")
            songs_titles = []
            for song in self.song_list:
                if song["title"] == title:
                    songs_titles.append(song)
            
            for song in songs_titles:
                print(f"✅✅ {song['song_id']}. {song['title']} - {song['artist']}")
            
            return
        
        elif choice == "artist":
            artist = input("------> Please enter artist: ")
            songs_artists = []
            for song in self.song_list:
                if song["artist"] == artist:
                    songs_artists.append(song)
            
            for song in songs_artists:
                print(f"✅✅ {song['song_id']}. {song['title']} - {song['artist']}")

            return
        
        elif choice == "genre":
            genre = input("------> Please enter genre: ")
            song_genres = []
            for song in self.song_list:
                if song["genre"] == genre:
                    song_genres.append(song)

            for song in song_genres:
                print(f"✅✅ {song['song_id']}. {song['title']} - {song['artist']}")
            
            return
        
        elif choice == "album":
            album = input("------> Please enter album: ")
            songs_albums = []
            for song in self.song_list:
                if song["album"] == album:
                    songs_albums.append(song)
            
            for song in songs_albums:
                print(f"✅✅ {song['song_id']}. {song['title']} - {song['artist']}")
            
            return
      
        elif choice == "length":
            length = input("------> Please enter length: ")
            songs_lengths = []
            for song in self.song_list:
                if song["length"] == length:
                    songs_lengths.append(song)
            
            for song in songs_lengths:
                print(f"✅✅ {song['song_id']}. {song['title']} - {song['artist']}")
            
            return
        
        else:
            print("Invalid choice")
            
            return
        
    def delete_song(self):
        
        for song in self.song_list:
            print(f"✅✅ {song['song_id']}. {song['title']} - {song['artist']}")
        
        song_id = int(input("------> Please enter song id you want to delete: "))
        self.song_list.pop(song_id - 1)

        try:
            with open('MusicStreaming/music.csv', 'r') as file:
                rows = list(csv.reader(file))
        except FileNotFoundError:
            print("File not found")
            return
        
        if 0 < song_id <= len(rows):
            
            del rows[song_id]

            with open('MusicStreaming/music.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

    def display_library(self):
        for song in self.song_list:
            print(f"✅✅ {song['song_id']}. {song['title']} - {song['artist']}")


class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.song_list = MusicLibrary().song_list
        self.song_info = {}
        self.shuffled_playlist = []

        # Create the playlist file if it does not exist
        file_path = f"MusicStreaming/{self.playlist_name}.csv"
        if not os.path.exists(file_path):
            with open(file_path, 'w', newline=''):
                pass  # Create an empty file

        # Read the playlist from the file
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            self.playlist = list(reader)
            self.playlist = sorted(self.playlist, key=lambda song: song["song_id"])

    def add_song(self, playlist_name):

        for song in self.song_list:
            print(f"✅✅ {song['song_id']}. {song['title']} - {song['artist']}")

        song_id = int(input("------> Please enter song id you want to add: "))
        song_library = self.song_list[song_id - 1]
           
        if any(song_data["title"] == song_library["title"] and song_data["artist"] == song_library["artist"] for song_data in self.playlist):
            print("Song already exists")
            return 
        
        self.song_info = {
            "song_id": song_library['song_id'], 
            "title": song_library['title'],
            "artist": song_library['artist'],
            "album": song_library['album'],
            "genre": song_library['genre'],
            "length": song_library['length']
        }

        self.playlist.append(self.song_info)

        try:
            with open(f"MusicStreaming/{playlist_name}.csv" ,'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.song_info.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(self.song_info)
        except FileNotFoundError:
            print("File not found")
            return
        

    def remove_song(self, playlist_name):
        
        for song in self.playlist:
            print(f"✅✅ {song['song_id']}. {song['title']} - {song['artist']}")
        
        song_id = int(input("------> Please enter song id you want to remove: "))
        self.playlist.pop(song_id - 1)

        ask = input("------> Do you really want to delete (y/n) : ").lower()
        if ask == "y":
            try:
                with open(f"MusicStreaming/{playlist_name}.csv", "r") as file:
                    rows = list(csv.reader(file))
            except FileNotFoundError:
                print("File not found")
                return
            
            if 0 < song_id <= len(rows):
                
                del rows[song_id]

                with open(f"MusicStreaming/{playlist_name}.csv", 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
        else:
            print("Song not deleted")
            return


    def reorder_songs(self):
        
        self.shuffled_playlist = random.sample(self.playlist, len(self.playlist))
        for song in self.shuffled_playlist:
            print(f"✅✅ {song['song_id']}. {song['title']} - {song['artist']}")


    def display_playlist(self):
        
        for song in self.playlist:
            print(f"✅✅ {song['song_id']}. {song['title']} - {song['artist']}")


def main():

    library = MusicLibrary()

    while True:
        print("=================<< Welcome to Music Streaming App >>=================")
        print("\t\t ||      1. Add Song                ||")   
        print("\t\t ||      2. Search Song             ||")
        print("\t\t ||      3. Delete Song             ||")
        print("\t\t ||      4. Display Library         ||")
        print("\t\t ||      5. Create Playlist         ||")
        print("\t\t ||      6. Existing Playlists      ||")
        print("\t\t ||      7. Exit                    ||")
        print("=================<< ------------------------------- >>=================")
        choice = int(input("Please enter your choice: "))
        print("=================<< ------------------------------- >>=================")

        if choice == 1:
            title = input("------> Please enter title: ")
            artist = input("------> Please enter artist: ")
            album = input("------> Please enter album: ")
            genre = input("------> Please enter genre: ")
            length = input("------> Please enter length: ")

            song = Song(title, artist, album, genre, length)
            library.add_song(song)

        elif choice == 2:
            library.search_song()
            print()

        elif choice == 3:
            library.delete_song()
            print()
        
        elif choice == 4:
            library.display_library()
            print()

        elif choice == 5:
            playlist_name = input("------> Please enter playlist name: ")
            playlist = Playlist(playlist_name)
            
            while True:
                print("=================<< ------------------------------- >>=================")
                print("1. Add Song")
                print("2. Remove Song")
                print("3. Reorder Songs")
                print("4. Display Playlist")
                print("5. Exit")
                print("=================<< ------------------------------- >>=================")
                choice = int(input("Please enter your choice: "))
                print("=================<< ------------------------------- >>=================")

                if choice == 1:
                    playlist.add_song(playlist_name)
                    print()

                elif choice == 2:
                    playlist.remove_song(playlist_name)
                    print()

                elif choice == 3:
                    playlist.reorder_songs()
                    print()

                elif choice == 4:
                    playlist.display_playlist()
                    print()

                elif choice == 5:
                    break

                else:
                    print("Invalid choice")
                    continue

        elif choice == 6:
            playlist_name = input("------> Please enter playlist name: ")
            playlist = Playlist(playlist_name)                                                                                                                                                                                                                                                                                                                                               
            
            while True:
                print("=================<< ------------------------------- >>=================")
                print("1. Add Song")
                print("2. Remove Song")
                print("3. Reorder Songs")
                print("4. Display Playlist")
                print("5. Exit")
                print("=================<< ------------------------------- >>=================")
                choice = int(input("Please enter your choice: "))
                print("=================<< ------------------------------- >>=================")

                if choice == 1:
                    playlist.add_song(playlist_name)
                    print()

                elif choice == 2:
                    playlist.remove_song(playlist_name)
                    print()

                elif choice == 3:
                    playlist.reorder_songs()
                    print()

                elif choice == 4:
                    playlist.display_playlist()
                    print()

                elif choice == 5:
                    break

                else:
                    print("Invalid choice")
                    continue

        elif choice == 7:
            break

        else:
            print("Invalid choice")
            continue

main()










