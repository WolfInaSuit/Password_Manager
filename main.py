from cryptography.fernet import Fernet


class PasswordManager:

    # Defines basically constructor, 1st Step.

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    # Create a method that generate a key 🔑.

    def create_key(self, path):
        self.key = Fernet.generate_key()
    # Creates key 👆🏽 & also 👇🏽 this is what stores it into a file
        with open(path, 'wb') as f:
            f.write(self.key)

    # A bit of testing, never hurt noone. 💻

    # pm = PasswordManager()
    # pm.create_key("mykey.key")

    # Function for loading. Once you create a key & create a new password file and you save your password you want to be
    # able to decrypt it again with the same key so the existing key has to be loaded.

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    # Function for creating the password file.
    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                pass  # TODO: add password function

    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    # Adding Password

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    # the get_password method essentially gives us the password once we pass an identifier or a site.

    def get_password(self, site):
        return self.password_dict[site]


def main():
    password = {
        "email": "123456789",
        "facebook": "myfbpassword",
        "youtube": "helloword123",
        "something": "myfavoritepassword2k23"
    }

    pm = PasswordManager()

    # "GUI"/ Choice Panel Questions

    print(""" What do you want do?
    (1) Create a new key 🔑🎉
    (2) Load an existing key 🗝️🔐       
    (3) Create a new password file 🥳🆕📁
    (4) Load existing password file 🗄️💻
    (5) Add a new password 🆕🎉
    (6) Get a password ✅✔☑️
    (q) Quit 👋🏽🖖🏽✋🏽
    """)

    done = False

    while not done:

        # "GUI"/ Choice Panel Answers

        choice = input(" Enter your choice: ")
        if choice == "1":
            path = input(" Enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input(" Enter path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input(" Enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input(" Enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            site = input(" Enter the site: ")
            password = input(" Enter the password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input(" What site do you want: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "q":
            done = True
            print(" You are in the right hand 😌 Thank you come again,BYE! 👋🏽💫  ")
        else:
            print(" 🚨 Invalid choice ❌ ")


# Professional way to run 🏃🏽‍ our code


if __name__ == "__main__":
    main()
