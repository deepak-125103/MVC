from models.repos.album_repo import Album_repo
from models.albums import Album

def view_create_album():
    album_id=input("1. Enter album ID")
    title=input("Enter title")
    artist=input("Enter artist")
    new_album=Album(album_id,title,artist)
    ar=Album_repo()
    ar.create_album(new_album)
    view_all_album()

def view_update_album():
    album_id=input("2. Enter Album ID")
    title=input("Enter Title")
    artist=input("Enter Artist")
    um=Album(album_id,title,artist)
    ar=Album_repo()
    ar.update_album(album_id,um)
    view_all_album()

def view_delete_album():
    album_id=input("3. Enter Album ID")
    ar=Album_repo()
    ar.delete_album(album_id)
    view_album()


def view_all_album():
    """Fetches and displays all album types."""
    try:
        ar= Album_repo()
        ag=ar.get_all_album()
        if not ag:
            print(f"no album found.")
        else:
            print("album table data \n---")
            for li in ag:
                print(f"ID:{li.album_id}, Titel: {li.title}, artist: {li.artist}")
    except Exception as e:
        print(f"an error occurred: {e}")



def view_album(album_id: int):
    """Fetches and displays album types."""
    try:
        alb=Album_repo()
        am=alb.get_album(album_id)
        if am:
            print(f"ID:{am.album_id}, Title: {am.title}, artist: {am.artist}")
        else:
            print(f"No album type found with ID {album_id}.")
    except Exception as e:
        print(f"an error occurred: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("Press 1. Create Album : ")
    print("Press 2. Update album : ")
    print("Press 3. Delete Album")
    print("Press 4. View for all album type : ")
    print("Press 5. View album type by ID : ")
    choice = input("Enter your choice:")

    if choice == "1":
        view_create_album()
    elif choice == "2":
        view_update_album()
    elif choice == "3":
        view_delete_album()
    elif choice == "4":
        view_all_album()
    elif choice == "5":
        try:
            album_id = int(input("Enter album type ID: "))
            view_album(album_id)
        except ValueError:
            print("Envalid ID please enter numerical value")
    else:
        print("invalid choise. Please choose 1 or 2")
