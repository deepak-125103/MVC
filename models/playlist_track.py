class Playlist_Track:
    def __init__(self,playlist_track_id: int ,track_id: int):
        self.playlist_track_id=playlist_track_id
        self.track_id=track_id

    def __repr__(self):
        return Playlist_Track(f"ID={self.playlist_track_id}, ID:{self.track_id}")