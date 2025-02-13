def write_password_to_file(password, file_path="passwords.txt"):
    with open(file_path, "a") as file:
        file.write(password + "\n")


def read_passwords_from_file(file_path="passwords.txt"):
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return ()