import json

start = input("Type \"New\" for a new file, or \"Current\" to grab a current file (in the entries folder) ")

def get_new_info():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    address = input("Address: ")
    phone_num = input("Phone Number (000-000-0000 format): ")

    new_user = {
        "first_name":first_name,
        "last_name":last_name,
        "address":address,
        "phone_num":phone_num
    }

    with open(f"entries\\{first_name} {last_name}.json", "w+") as user_file:
        user_file.write(json.dumps(new_user))
        user_file.close()
    
    print("Made file! (restart program to check)")

def get_current_info():
    user_input = input("Please enter a name you want to search (first and last): ")

    try:
        user_file = open(f"entries\\{user_input}.json", "r+")
    except FileNotFoundError:
        print("Sorry, file not found! Please restart the program.")
        exit()

    global info_dict
    info_dict = json.loads(user_file.read())

    print("File found! Proceeding to next step...")

    user_input = input("Please enter the information you want to get. (First name, last name, address, phone number)")
    if user_input.lower() == "first name":
        print(info_dict["first_name"])
    elif user_input.lower() == "last name":
        print(info_dict["last_name"])
    elif user_input.lower() == "address":
        print(info_dict["address"])
    elif user_input.lower() == "phone number":
        print(info_dict["phone_num"])
    else:
        print("That\'s not a valid query!")
    

if start == "new":
    get_new_info()
elif start == "current":
    get_current_info()