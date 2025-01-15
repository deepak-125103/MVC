from models.genres import Genres
from models.repos.a_genres import AGenres
import sqlite3

class GenresRepo(AGenres):
    def create_genres(self, model: Genres) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"insert into genres values ({model.gener_id}, '{model.gener_name}')")
        except sqlite3.Error as e:
            print(f"Data base error {e}")
            
    
    def update_genres(self, gener_id: int, model: Genres) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update genres set Name= '{model.gener_name}' where GenreId ={gener_id}")
        except sqlite3.Error as e:
            print(f"Data base error {e}")

       
    def delete_genres(self, gener_id: int) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"delete from genres where GenreId={gener_id}")
        except sqlite3.Error as e:
            print(f"Database Error {e}")

    
    def get_genres(self, gener_id: int) -> Genres:
        try:
            conn=sqlite3.connect("chinook.db")
            print("chinook data base connected seccussfully")
            cursor=conn.execute("select * from genres WHERE Genreid=?",(gener_id,))
            row=cursor.fetchone()
            if row:
                return Genres(gener_id=row[0], gener_name=row[1])
                # return Genres(gener_id=row[0], gener_name=row[1])
            else:
                print(f"No gener found with ID {gener_id}")
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()


    def get_all_genres(self) -> list[Genres]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("select * from Genres")
                for row in cursor:
                    g = Genres(gener_id=row[0], gener_name= row[1])
                    data_list.append(g)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list