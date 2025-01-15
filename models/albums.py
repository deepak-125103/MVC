class Album:
    def __init__(self,album_id: int, title: str,artist:int):
        self.album_id=album_id
        self.title=title
        self.artist=artist

    def __repr__(self):
        return f"Album(id:{ self.album_id}, title:{self.title}, artist:{self.artist})"