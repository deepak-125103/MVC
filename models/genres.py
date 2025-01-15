class Genres:
    def __init__(self, gener_id: int, gener_name: str):
        self.gener_id = gener_id
        self.gener_name = gener_name

    def __repr__(self):
        return f"Genres(id={self.gener_id} name={self.gener_name})"