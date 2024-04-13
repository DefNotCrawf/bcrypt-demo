def is_string_blank(s):
    if not s or s.strip() == "":  # false blank string
        # print("blank")
        return False
    else:  # true has string
        return True


def first_register_username():
    while True:
        print("Hello user.")
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


def name_and_pass_to_csv():
    user_name, user_pass = first_register()
    with open(r"plain_text.csv", "a") as file:
        file.write(f"\n{user_name},{user_pass}")


i = 0


def login(i):
    while i < 2:
        intput_username = input("Please enter your username: ")
        intput_password = input("Please enter your password: ")
        with open(r"plain_text.csv", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                if username == intput_username and password == intput_password:
                    print("Login successful.")
                    return True, username
            else:
                i += 1
                print("Login failed. Please try again.")
                continue
    else:
        while i < 3:
            intput_username = input("Please enter your username: ")
            intput_password = input("Please enter your password: ")
            with open(r"plain_text.csv", "r") as file:
                for line in file:
                    username, password = line.strip().split(",")
                    if username == intput_username and password == intput_password:
                        print("Login successful.")
                        return True, username
                else:
                    i += 1
                    print("Login failed.")
                    return False, None


def menu_signed_in(user):
    print(f"Hello {user}!")
    while True:
        print("1. Change Password", "2. Logout", sep="\n")
        choice = input("Please select an option: ")
        if choice in ["1", "2"]:
            match choice:
                case "1":
                    change_password(user)
                case "2":
                    print("Logout successful.")
                    break
        else:
            print("Invalid option. Please try again.")
            continue


def change_password(user):
    new_pass = input("Please enter a new password: ")
    with open(r"plain_text.csv", "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            if username == user:
                with open(r"plain_text.csv", "r") as file:
                    lines = file.readlines()
                with open(r"plain_text.csv", "w") as file:
                    for line in lines:
                        if line.strip() == f"{username},{password}":
                            file.write(f"\n{username},{new_pass}")
                        else:
                            file.write(line)


def menu_not_signed_in(i):
    while True:
        print("1. Register", "2. Login", "3. Exit", sep="\n")
        choice = input("Please select an option: ")
        if choice in ["1", "2", "3"]:
            match choice:
                case "1":
                    name_and_pass_to_csv()
                    menu_not_signed_in(i)
                case "2":
                    result_bool, username = login(i)
                    if result_bool:
                        menu_signed_in(username)
                    else:
                        exit()
                case "3":
                    print("exit")
                    exit()
        else:
            print("Invalid option. Please try again.")


menu_not_signed_in(i)

