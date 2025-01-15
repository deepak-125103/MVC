from models.playlists import Playlist
from models.repos.a_playlist import A_playlist
import sqlite3

class Plist_repo(A_playlist):

    def create_palylist(self, model: Playlist)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"insert into playlists values({model.playlist_id},'{model.palylist_name}')")
        except sqlite3.Error as e:
            print(f"Database error {e}")
    
   
    def upadate_playlist(self, playlist_id: int, model:  Playlist)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update playlists set Name='{model.palylist_name}' WHERE PlaylistId={playlist_id}")
        except sqlite3.Error as e:
            print(f"Database Error {e}")

   
    def delete_playlist(self,playlist_id: int)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"delete from playlists WHERE PlaylistId={playlist_id}")
        except sqlite3.Error as e:
            print(f"Database Error {e}")

    
    def get_playlist(self, playlist_id: int)-> Playlist:
        try:
           conn=sqlite3.connect("chinook.db")
           print("Database connected successfully")
           cursor=conn.execute("select * from playlists WHERE Playlistid=?",(playlist_id,))
           row=cursor.fetchone()
           if row:
               return Playlist(playlist_id=row[0],palylist_name=row[1])
           else:
               print(f"No playlist found with ID {playlist_id}")
               return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()

    
    def get_all_palylist(self)->list[Playlist]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor=conn.execute("select * from playlists")
                for row in cursor:
                    gap=Playlist(playlist_id=row[0],palylist_name=row[1])
                    data_list.append(gap)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list       