from models.repos.palylist_repo import Plist_repo
from models.playlists import Playlist

def view_create_palylist():
    playlist_id=input("1. Enter Play list  ID : ")
    palylist_name=input("Enter Name ID : ")
    new_playlist=Playlist(playlist_id, palylist_name)
    plr=Plist_repo()
    plr.create_palylist(new_playlist)
    view_playlist()

def view_upadate_playlist():
    playlist_id=input("2. Enter playlist  ID : ")
    palylist_name=input("Enter Name ID : ")
    upl=Playlist(playlist_id,palylist_name)
    plr=Plist_repo()
    plr.upadate_playlist(playlist_id,upl)
    view_playlist()

def view_delete_playlist():
    playlist_id=input("3. Enter Play list  ID : ")
    plr=Plist_repo()
    plr.delete_playlist(playlist_id)
    view_playlist()


def view_playlist():
    """Fetches and displays all gener types."""
    try:
        pl=Plist_repo()
        plp=pl.get_all_palylist()
        if not plp:
            print("NO play list found")
        else:
            print("Playlist data \n----")
            for li in plp:
                print(f"ID:{li.playlist_id}, Name: {li.palylist_name}")
    except Exception as e:
        print(f"an error occurred: {e}")




def view_playlist_id(playlist_id: int):
    """Fetches and displays genres types."""
    try:
        vpd=Plist_repo()
        vpr=vpd.get_playlist(playlist_id)
        if vpr:
            print(f"ID: {vpr.playlist_id}, Name: {vpr.palylist_name}")
        else:
            print(f"No gener type found with ID {playlist_id}.")
    except Exception as e:
        print(f"an error occurred: {e}")
    
if __name__=="__main__":
    print("Choose an option")
    print("Press 1. view Create Play list ID :")
    print("Press 2. Update Play list  ID : ")
    print("Press 3. Delete Play list  ID : ")
    print("Press 4. View for all playlist")
    print("Press 5. View playlist with ID")
    choice=input("Enter your choice:")

    if choice=="1":
        view_create_palylist()
    elif choice=="2":
        view_upadate_playlist()
    elif choice=="3":
        view_delete_playlist()
    elif choice=="4":
        view_playlist()
    elif choice=="5":
        try:
            playlist_id=int(input("Enter playlist ID: "))
            view_playlist_id(playlist_id)
        except ValueError:
            print("Envalid ID please enter numerical value")
    else:
        print("invalid choise. Please choose an option 1 to 5")