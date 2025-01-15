from models.media_type import MediaType
from models.repos.a_media_type import AMediaType
import sqlite3

class MediaTypeRepo(AMediaType):
    def create_media_type(self, model: MediaType) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f" insert into media_types values( {model.media_type_id}, '{model.media_type_name}')")
        except sqlite3.Error as e:
            print(f"Database error: {e}")



    def update_media_type(self, media_type_id: int, model: MediaType) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update media_types set Name='{model.media_type_name}' where MediaTypeId={media_type_id}")
        except sqlite3.Error as e:
            print(f"Databse error: {e}")


    def delete_media_type(self, media_type_id: int) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"delete from media_types where MediaTypeId={media_type_id}")
        except sqlite3.Error as e:
            print(f"databse error : {e}")


 
    def get_media_type(self, media_type_id: int) -> MediaType:
        try:
            conn=sqlite3.connect("chinook.db")
            print("chinook data base connected successfully")
            cursor=conn.execute("select * from media_types WHERE MediaTypeId=?",(media_type_id,))
            row= cursor.fetchone()
            if row:
                return MediaType(media_type_id=row[0], media_type_name=row[1])
            else:
                print(f"NO mediya tyoe found with ID: {media_type_id}")
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()

        

    def get_all_media_types(self) -> list[MediaType]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM media_types")
                for row in cursor:
                    mt = MediaType(media_type_id=row[0], media_type_name=row[1])
                    data_list.append(mt)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
