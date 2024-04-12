def is_string_blank(s):
    if not s or s.strip() == "":  # false blank string
        # print("blank")
        return False
    else:  # true has string
        return True


def first_register_username():
    while True:
        print("Hello user.")
        print("You have not registered.")
        uName = input("Please enter a username: ")
        if is_string_blank(uName):
            # print("success")
            return uName
        else:
            print("Invalid username. Please try again.")
            continue


def first_register_password(name):
    while True:
        print(f"Hello '{name}'!")
        uPass = input("Please enter a password: ")
        if is_string_blank(uPass):
            # print("success")
            return uPass
        else:
            print("Invalid password. Please try again.")
            continue


def first_register():
    userName = first_register_username()
    userPass = first_register_password(userName)
    return userName, userPass


def name_and_pass_to_txt():
    user_name, user_pass = first_register()
    with open(r"plain_text.txt", "a") as file:
        file.write(f"\n{user_name},{user_pass}")


def menu_not_signed_in():
    print("1. Register", "2. Login", "3. Exit", sep="\n")
    choice = input("Please select an option: ")
    if choice in ["1", "2", "3"]:
        print("options sel")
        match choice:
            case "1":
                name_and_pass_to_txt()
            case "2":
                print("login")
            case "3":
                print("exit")
                exit()
    else:
        print("Invalid option. Please try again.")


menu_not_signed_in()
