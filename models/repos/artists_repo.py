from models.artists import Artist
from models.repos.a_artists import A_artist
import sqlite3

class artist_repo(A_artist):
    def creat_artist(self, model: Artist)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"insert into artists values({model.artist_id},'{model.artist_name}')")
        except sqlite3.Error as e:
            print(f"Database Error {e}")

    def update_artist(self, artist_id: int, model: Artist)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update artists set Name='{model.artist_name}' where ArtistId={artist_id}")
        except sqlite3.Error as e:
            print(f"Database error {e}")

    def delet_artist(self, artist_id: int)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"delete from artists where ArtistId={artist_id}")
        except sqlite3.Error as e:
            print(f"Database Error {e}")

    def get_artist(self, artist_id: int)-> Artist:
        try:
            conn=sqlite3.connect("chinook.db")
            print("Data abse is connected successfully")
            cursor=conn.execute("select * from artists WHERE ArtistId=?",(artist_id,))
            row= cursor.fetchone()
            if row :
                return Artist(artist_id=row[0], artist_name=row[1])
            else:
                print("No Artist found with ID")
                return None
        except sqlite3.Error as e:
           print(f"Data base Error {e}")
           return None
        finally:
           conn.close()
               
           
    
    def get_all_artist(self)->list[Artist]:
        data_list=[]
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor= conn.execute("select *from artists")
                for row in cursor:
                    ad = Artist(artist_id=row[0], artist_name=row[1])
                    data_list.append(ad)
        except sqlite3.Error as e:
            print(f"Database Error {e}")
        return data_list
