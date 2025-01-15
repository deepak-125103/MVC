from models.repos.Track_repo import TrackRepo
from models.tracks import Track

def view_create_track():
    track_id=input("1. Enter Track ID :")
    track_name=input("Enter Track Nmae :")
    album_id=input("Enter Album ID :")
    media_type_id=input("Enter media type ID :")
    GenreId=input("Genre ID :")
    composer=input("Enter Composer :")
    mili_sec=input("Enter Milli sec :")
    bytes=input("Enter Bytes :")
    unit_price=input("Enter Unit price :")
    new_track=Track(track_id,track_name,album_id,media_type_id,GenreId,composer,mili_sec,bytes,unit_price,)
    tr=TrackRepo()
    tr.creat_tracks(new_track)
    view_all_track()

def view_update_track():
    track_id=input("2. Enter Track ID :")
    track_name=input("Enter Track Nmae :")
    album_id=input("Enter Album ID :")
    media_type_id=input("Enter media type ID :")
    GenreId=input("Genre ID :")
    composer=input("Enter Composer :")
    mili_sec=input("Enter Milli sec :")
    bytes=input("Enter Bytes :")
    unit_price=input("Enter Unit price :")
    ut=Track(track_id,track_name,album_id,media_type_id,GenreId,composer,mili_sec,bytes,unit_price,)
    tr=TrackRepo()
    tr.update_tracks(track_id,ut)
    view_all_track()

def view_delete_track():
    track_id=input(". Enter Track ID :")
    tr=TrackRepo()
    tr.delete_track(track_id)
    view_all_track()


def view_all_track():
    """Fetches and displays all gener types."""
    try:
        Tr=TrackRepo()
        Tv=Tr.get_all_track()
        if not Tv:
            print(f"no track found.")
        else:
            print("Track table data \n---")
            for li in Tv:
                print(f"ID:{li.track_id}, Name:{li.track_name}, AlbumID:{li.album_id},MediaTypeId:{li.media_type_id}, GenreId:{li.GenreId},Composer:{ li.composer}, Milisecond:{li.mili_sec}, Bytes:{li.bytes},Unit Price:{li.unit_price})")
    except Exception as e:
        print(f"an error occurred: {e}")
 

def view_Tracks(track_id: int):
    """Fetches and displays genres types."""
    try:
        Gt=TrackRepo()
        Ggt=Gt.get_track(track_id)
        if Ggt:
            print(f"ID: {Ggt.track_id}, Name:{Ggt.track_name},  AlbumID:{Ggt.album_id},MediaTypeId:{Ggt.media_type_id},GenreId:{Ggt.GenreId},Composer:{ Ggt.composer}, Milisecond:{Ggt.mili_sec}, Bytes:{Ggt.bytes},Unit Price:{Ggt.unit_price})")
        else:
            print(f"No gener type found with ID {track_id}.")
    except Exception as e:
        print(f"an error occurred: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("Press 1. View for Create Track type ")
    print("Press 2. View for Update Track type ")
    print("Press 3. View for Delete Track type ")
    print("Press 4. View for all Track type ")
    print("Press 5. View track by ID")
    choice = input("Enter your choice:")

    if choice == "1":
        view_create_track()
    elif choice == "2":
        view_update_track()
    elif choice=="3":
        view_delete_track()
    elif choice=="4":
        view_all_track()
    elif choice=="5":
        try:
            track_id = int(input("Enter Track type ID: "))
            view_Tracks(track_id)
        except ValueError:
            print("Envalid ID please enter numerical value")
    else:
        print("invalid choise. Please choose an option between 1 to 5")

