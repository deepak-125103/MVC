from models.albums import Album
from models.repos.a_album import abs_album
import sqlite3

class Album_repo(abs_album):
    def create_album(self, model: Album)-> None:
        try:
            with sqlite3.connect("chinook.db")as conn:
                conn.execute(f" insert into albums values({model.album_id},'{model.title}','{model.artist}')")
        except sqlite3.Error as e:
            print(f"Database Error: {e}")


    def update_album(self, album_id: int, model: Album)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update albums set Title= '{model.title}',  ArtistId='{model.artist}' WHERE AlbumId={album_id}")
        except sqlite3.Error as e:
            print(f"Database Error {e}")

    def delete_album(self, album_id:int)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"delete from albums WHERE AlbumId={album_id}")
        except sqlite3.Error as e:
            print(f"Databse Error {e}")

    def get_album(self, album_id: int)-> Album:
        try:
            conn=sqlite3.connect("chinook.db")
            print("chinook data base connected seccussfully")
            cursor=conn.execute("select * from albums WHERE AlbumId=?",(album_id,))
            row=cursor.fetchone()
            if row:
                return Album(album_id=row[0], title=row[1],artist=row[2])
                
            else:
                print(f"No album found with ID {album_id}")
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()


    def get_all_album(self)-> list[Album]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("select * from albums")
                for row in cursor:
                    ga = Album(album_id=row[0], title=row[1],artist=row[2] )
                    data_list.append(ga)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list