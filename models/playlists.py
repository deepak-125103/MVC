class Playlist:
    def __init__(self,playlist_id: int, palylist_name: str):
        self.playlist_id=playlist_id
        self.palylist_name=palylist_name
    
    def __repr__(self):
        return f"Playlist(id={self.playlist_id}, name={self.palylist_name})"
