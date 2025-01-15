from models.playlist_track import Playlist_Track
from models.repos.a_playlist_track import A_pl_track
import sqlite3

class APL_track(A_pl_track):

    def creat_playlist_track(self,model:Playlist_Track)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"insert into playlist_track values({model.playlist_track_id},'{model.track_id}')")
        except sqlite3.Error as e:
            print(f"Database error {e}")


    def update_playlist_track(self,playlist_track_id: int,model: Playlist_Track)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update playlist_track set TrackId={model.track_id} WHERE PlaylistId={playlist_track_id}")
        except sqlite3.Error as e:
            print(f"Database Error {e}")

   
    def delete_playlist_track(self,playlist_track_id: int)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"delete from playlist_track WHERE PlaylistId={playlist_track_id}")
        except sqlite3.Error as e:
            print(f"Database Error {e}")

    
    def get_playlist_track(self,playlist_track_id: int)->Playlist_Track:
        try:
            conn=sqlite3.connect("chinook.db")
            print("Database is connected successfully")
            corsur=conn.execute("select * from playlist_track WHERE PlaylistId=?",(playlist_track_id,))
            row=corsur.fetchone()
            if row:
                return Playlist_Track(playlist_track_id=row[0],track_id=row[1])
            else:
                print("No play list tack found with ID")
                return None
        except sqlite3.Error as e:
            print(f"Database Error :{e}")
            return None
        finally:
            conn.close()


    def get_all_playlist_track(self)->list[Playlist_Track]:
        data_list=[]
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor=conn.execute("select * from playlist_track")
                for row in cursor:
                    gpt=Playlist_Track(playlist_track_id=row[0],track_id=row[1])
                    data_list.append(gpt)
        except sqlite3.Error as e:
            print(f"Databse Error ID:{e}")
        return data_list

        