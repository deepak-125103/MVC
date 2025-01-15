class Track:
    def __init__(self,track_id: int,track_name:str, album_id:int,media_type_id,GenreId,composer:str, mili_sec:int, bytes:int, unit_price:None,):
        self.track_id=track_id
        self.track_name=track_name
        self.album_id=album_id
        self.media_type_id=media_type_id
        self.GenreId=GenreId
        self.composer=composer
        self.mili_sec=mili_sec
        self.bytes=bytes
        self.unit_price=unit_price

        

    def __repr__(self):
        return f"Track(id={self.track_id}, Name:{self.track_name}, AlbumID:{self.album_id},Media Type ID: {self.media_type_id},GemreID;{self.GenreId},Composer:{ self.composer}, Milisecond:{self.mili_sec}, Bytes:{self.bytes},Unit Price:{self.unit_price})"
    







    # class Track:
    # def __init__(self,track_id: int):
    #     self.track_id=track_id

    # def __repr__(self):
    #     return f"Track(id={self.track_id})"