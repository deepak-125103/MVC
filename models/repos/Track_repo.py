from models.tracks import Track
from models.repos.a_tracks import A_Track
import sqlite3

class TrackRepo(A_Track):
    def creat_tracks(self, model: Track)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"insert into tracks values('{model.track_id}','{model.track_name}','{model.album_id}','{model.media_type_id}','{model.GenreId}','{model.composer}','{model.mili_sec}','{model.bytes}','{model.unit_price}')")
        except sqlite3.Error as e:
            print(f"Data base error {e}")

    def update_tracks(self, track_id: int, model: Track)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update tracks set Name='{model.track_name}',AlbumId='{model.album_id}',MediaTypeId='{model.media_type_id}',GenreId='{model.GenreId}',Composer='{model.composer}',Milliseconds='{model.mili_sec}',Bytes='{model.bytes}',UnitPrice='{model.unit_price}' where TrackId={track_id}")
        except sqlite3.Error as e:
            print(f"Data base Error {e}")

    def delete_track(self, track_id: int)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"delete from tracks WHERE TrackId={track_id}")
        except sqlite3.Error as e:
            print(f"Data base Error {e}")

    def get_track(self, track_id:int)-> Track:
        try:
            conn=sqlite3.connect("chinook.db")
            print("chinook data base connected seccussfully")
            cursor=conn.execute("select * from tracks WHERE TrackId=?",(track_id,))
            row= cursor.fetchone()
            if row:
                return Track(track_id=row[0],track_name=row[1],album_id=row[2],media_type_id=row[3],GenreId=row[4], composer=row[5],mili_sec=row[6],bytes=row[7],unit_price=row[8])
                
            else:
                print(f"No Track found with ID {track_id}")
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()


    def get_all_track(self)-> list[Track]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("select * from tracks")
                for row in cursor:
                    T= Track(track_id=row[0], track_name=row[1],album_id=row[2],media_type_id=row[3],GenreId=row[4], composer=row[5],mili_sec=row[6],bytes=row[7],unit_price=row[8])
                    data_list.append(T)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
    













#     from models.tracks import Track
# from models.repos.a_tracks import A_Track
# import sqlite3

# class TrackRepo(A_Track):
#     def creat_tracks(self, model: Track)-> None:
#         pass

#     def update_tracks(self, tr_id: int, model: Track)-> None:
#         pass
    
#     def delete_track(self, tr_id: int)-> None:
#         pass

#     def get_track(self, tr_id:int)-> Track:
#         try:
#             conn=sqlite3.connect("chinook.db")
#             print("chinook data base connected seccussfully")
#             cursor=conn.execute("select * from tracks WHERE TrackId=?",(tr_id,))
#             row= cursor.fetchone()
#             if row:
#                 return Track(track_id=row[0])
                
#             else:
#                 print(f"No Track found with ID {tr_id}")
#                 return None
#         except sqlite3.Error as e:
#             print(f"Database error: {e}")
#             return None
#         finally:
#             conn.close()


        

#     def get_all_track(self)-> list[Track]:
#         data_list = []
#         try:
#             with sqlite3.connect("chinook.db") as conn:
#                 cursor = conn.execute("select * from tracks")
#                 for row in cursor:
#                     T= Track(track_id=row[0])
#                     data_list.append(T)
#         except sqlite3.Error as e:
#             print(f"Database error: {e}")
#         return data_list