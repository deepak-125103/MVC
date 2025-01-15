from models.repos.artists_repo import artist_repo
from models.artists import Artist

def view_create_artist():
    artist_id=input("1. Enter Artist ID : ")
    artist_name=input("Enter Artist Name : ")
    new_artist=Artist(artist_id,artist_name)
    ar=artist_repo()
    ar.creat_artist(new_artist)
    All_Artist()

def view_update_artist():
    artist_id=input("2. Enter artist ID : ")
    artist_name=input("Enter artist name : ")
    ua=Artist(artist_id,artist_name)
    uar=artist_repo()
    uar.update_artist(artist_id,ua)
    All_Artist()

def delete_artist():
    artist_id=input("3. Enter artist ID : ")
    ar=artist_repo()
    ar.delet_artist(artist_id)
    All_Artist()

def All_Artist():
    '''Fetch and display all Artist'''
    try:
        AA= artist_repo()
        gaa=AA.get_all_artist()
        if not gaa:
            print("No artist found.")
        else:
            print("Artist Tabel data \n-----")
            for li in gaa:
                print(f"ID:{li.artist_id}, Name:{li.artist_name}")
    except Exception as e:
        print(f"An Error occured: {e}")


def one_artist(artist_id: int):
    '''Fetch and Display Artist by ID '''
    try:
        Ar=artist_repo()
        oa=Ar.get_artist(artist_id)
        if oa:
            print(f"ID:{oa.artist_id}, Name:{oa.artist_name}")
        else:
            print(f"No artist found with ID ={artist_id}.")
    except Exception as e:
        print(f"En error Occured: {e} ")

if __name__=="__main__":
    print("Choose an option")
    print("Press 1. for Create artist ID : ")
    print("Press 2. for update artist :  ")
    print("Press 3. delete artist :")
    print("Press 4. for list of all artist.")
    print("Press 5. for artis by ID ")
    choice=input("Enter yur choice : ")

    if choice=="1":
        view_create_artist()
    elif choice=="2":
        view_update_artist()
    elif choice=="3":
        delete_artist()
    elif choice=="4":
        All_Artist()
    elif choice=="5":
        try:
            ar_id=int(input("Enter artist ID : "))
            one_artist(ar_id)
        except ValueError:
            print("invalid id please enter numerical value")
    else:
        print("invalid choice. Please choose  an option 1 upto 5 ")