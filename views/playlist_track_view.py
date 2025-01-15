from models.repos.playlist_track_repo import APL_track
from models.playlist_track import Playlist_Track

def view_create_playlist_track():
    playlist_track_id=input("1. Enter Play list track ID : ")
    track_id=input("Enter track ID : ")
    new_playlist_track=Playlist_Track(playlist_track_id, track_id)
    pltr=APL_track()
    pltr.creat_playlist_track(new_playlist_track)
    view_all_playlist_track()

def view_update_playlist_track():
    playlist_track_id=input("2. Enter playlist track ID : ")
    track_id=input("Enter track ID : ")
    uplt=Playlist_Track(playlist_track_id,track_id)
    pltr=APL_track()
    pltr.update_playlist_track(playlist_track_id,uplt)
    view_all_playlist_track()

def view_delete_playlist_track():
    playlist_track_id=input("3. Enter Play list track ID : ")
    pltr=APL_track()
    pltr.delete_playlist_track(playlist_track_id)
    view_all_playlist_track()


def view_all_playlist_track():
    '''Fetches and display all play list track'''
    try:
        Plt= APL_track()
        vplt=Plt.get_all_playlist_track()
        if not vplt:
            print("No Play list track found")
        else:
            print("Play list track data \n-------")
            for li in vplt:
                print(f"ID:{li.playlist_track_id},track ID: {li.track_id}")
    except Exception as e:
        print(f"an error occurred: {e}")



def view_playlist_track(playlist_track_id: int):
    '''Fatch and display playlist track'''
    try:
        vpt=APL_track()
        pt=vpt.get_playlist_track(playlist_track_id)
        if pt:
            print(f"ID: {pt.playlist_track_id}, Track ID: {pt.track_id}")
        else:
            print(f"No play list track ID found {playlist_track_id}.")
    except Exception as e:
        print(f"an error occurred: {e}")
    
if __name__=="__main__":
    print("Choose an option")
    print("Press 1. view Create Play list track ID :")
    print("Press 2. Update Play list track ID : ")
    print("Press 3. Delete Play list track ID : ")
    print("Press 4. View all Play list track ID : ")
    print("Press 5. view play list track with ID : ")
    choice= input("Enter your chioice : ")

    if choice== "1":
       view_create_playlist_track()
    elif choice=="2":
        view_update_playlist_track()
    elif choice=="3":
        view_delete_playlist_track()
    elif choice=="4":
        view_all_playlist_track()
    elif choice=="5":
        try:
            playlist_track_id=int(input("Enter play list track id: "))
            view_playlist_track(playlist_track_id)
        except ValueError:
            print("invalid ID please enter numerical value.")
    else:
        print("Invalid choice. Please choose an option between 1 to 5 ")
