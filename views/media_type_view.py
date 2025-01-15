from models.repos.media_type_repo import MediaTypeRepo
from models.media_type import MediaType

def view_create_media_type():
    media_type_id=input("1. Enter Media Type ID: ")
    media_type_name=input("Enter Media Type Name: ")
    new_media_id=MediaType(media_type_id,media_type_name)
    mtr=MediaTypeRepo()
    mtr.create_media_type(new_media_id)
    view_media_type()


def view_update_media_type():
    media_type_id=input("2. Enter Media Type ID: ")
    media_type_name=input("Enter Media Type Name: ")
    umt=MediaType(media_type_id,media_type_name)
    mtr=MediaTypeRepo()
    mtr.update_media_type(media_type_id,umt)
    view_media_type()


def view_delete_media_type():
    media_type_id=input("3.Enter Media Type ID: ")
    mtr=MediaTypeRepo()
    mtr.delete_media_type(media_type_id)
    view_media_type()

def view_media_type():
    """Fetches and displays all media types."""
    try:
        mtr = MediaTypeRepo()
        gamt = mtr.get_all_media_types()
        if not gamt:
            print("No media types found.")
        else:
            for li in gamt:
                print(f"Id: {li.media_type_id}, Name: {li.media_type_name}")
    except Exception as e:
        print(f"An error occurred: {e}")



def get_media_type(mt_id:int):
    """Fetch and display media"""
    try:
        gmt=MediaTypeRepo()
        gt=gmt.get_media_type(mt_id)
        if gt:
            print(f" ID: {gt.media_type_id}, Name:{gt.media_type_name}")
        else:
            print(f"NO media type found with ID {mt_id}")
    except Exception as e:
        print(f"an error occurred: {e}")

if __name__=="__main__":
    print("Choose an option")
    print("Press 1. for Creat media type by ID")
    print("Press 2. for Update media type by ID")
    print("Press 3. for Delete media type ID")
    print("Press 4. for View all media type")
    print("Press 5. for View media type bye ID")
    choice= input("Enter a choice: ")

    if choice == "1":
        # choice= input("Enter a choice for create Media Type:")
        view_create_media_type()

    elif choice == "2":
        # choice= input("Enter a choice for update media type:")
        view_update_media_type()

    elif choice =="3":
        # choice= input("Enter a choice for delete Media type:")
        view_delete_media_type()

    elif choice =="4":
        # choice= input("Enter a choice for get all media type:")
        view_media_type()

    elif choice =="5":
        # choice= input("Enter a choice for get media type by ID:")
        try:
            mt_id= int(input("Enter media type ID: "))
            get_media_type(mt_id)
        except ValueError:
            print("Envalid ID please enter numerical value")
    else:
        print("invalid choise. Please choose 1 or 2")
    


# if __name__=="__main__":
#     print("Choose an option")
#     print("Press 1. view all media type")
#     print("Press 2. view media by ID")
#     choice= input("Enter a choice:")

#     if choice == "1":
#         view_media_type()
#     elif choice == "2":
#         try:
#             mt_id= int(input("Enter media type ID: "))
#             get_media_type(mt_id)
#         except ValueError:
#             print("Envalid ID please enter numerical value")
#     else:
#         print("invalid choise. Please choose 1 or 2")
