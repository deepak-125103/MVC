from models.repos.genres_repo import GenresRepo
from models.genres import Genres

def view_create_genres():
    gener_id=input("1. Enter Gener iD: ")
    gener_name=input(" Enter Genre Name: ")
    new_gener=Genres(gener_id,gener_name)
    gr=GenresRepo()
    gr.create_genres(new_gener)
    view_genres_type()

def view_update_gener():
    gener_id=input("2. Enter Gener ID")
    gener_name=input("Enter Gener Name")
    ug=Genres(gener_id,gener_name)
    ugr=GenresRepo()
    ugr.update_genres(gener_id,ug)
    view_genres_type()

def view_delete_gener():
    gener_id=input("3. Enter Gener ID")
    gr=GenresRepo()
    gr.delete_genres(gener_id)
    view_genres_type()


def view_genres_type():
    """Fetches and displays all gener types."""
    try:
        gr= GenresRepo()
        gag=gr.get_all_genres()
        if not gag:
            print(f"no genres found.")
        else:
            print("Gener table data \n---")
            for li in gag:
                print(f"ID:{li.gener_id}, Name: {li.gener_name}")
    except Exception as e:
        print(f"an error occurred: {e}")

 

def view_genres(gener_id: int):
    """Fetches and displays genres types."""
    try:
        gnr=GenresRepo()
        gr=gnr.get_genres(gener_id)
        if gr:
            print(f"ID: {gr.gener_id}, Name: {gr.gener_name}")
        else:
            print(f"No gener type found with ID {gener_id}.")
    except Exception as e:
        print(f"an error occurred: {e}")


if __name__ == "__main__":
    print("Choose an option")
    print("Press 1. for Creat Geners by ID")
    print("Press 2. for Update Geners by ID")
    print("Press 3. for Delete Geners ID")
    print("Press 4. for View all Gener")
    print("Press 5. for View Geners bye ID")
    choice= input("Enter a choice: ")

    if choice=="1":
       view_create_genres()
    elif choice=="2" :
        view_update_gener()
    elif choice=="3":
        view_delete_gener()
    elif choice=="4":
        view_genres_type()
    elif choice=="5":
        try:
            gener_id= int(input("Enter Gener ID: "))
            view_genres(gener_id)
        except ValueError:
            print("Envalid ID please enter numerical value")
    else:
        print("invalid choise. Please choose 1 or 2")
    

# if __name__ == "__main__":
#     print("Choose an option:")
#     print("Press 1. View for all Gener type ")
#     print("Press 2. View Gener type by ID")
#     choice = input("Enter your choice:")

#     if choice == "1":
#         view_genres_type()
#     elif choice == "2":
#         try:
#             g_id = int(input("Enter Gener type ID: "))
#             view_genres(g_id)
#         except ValueError:
#             print("Envalid ID please enter numerical value")
#     else:
#         print("invalid choise. Please choose 1 or 2")
