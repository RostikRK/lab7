from numpy import place
import auth
import menu


class Interaction:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "create": self.create_account,
            "quit": self.quit,
        }
        self.admin_map = {
            "notebook": self.go_to_notebook,
            "change": self.change_permission,
            "delete": self.delete_user,
            "logout": self.menu,
        }

    def create_account(self):
        indenificator = False
        while indenificator == False:
            username = input("username: ")
            password = input("password: ")
            try:
                auth.authenticator.add_user(username, password)
                indenificator = True
            except auth.TooShortname:
                print("You shoul enter some name")
            except auth.UsernameAlreadyExists:
                print("This username is already exist")
            except auth.PasswordTooShort:
                print("Password should contain at least 6 characters")

    def go_to_notebook(self):
        menu.AdminMenu().run()

    def change_permission(self):
        print("You are in all users permission settings")
        indenificator = False
        while indenificator == False:
            username = input("username whose permission you want to change:")
            permission = input("to which permission change:")
            try:
                auth.authorizor.change_permission(permission, username)
                indenificator = True
            except auth.InvalidUsername:
                print("You entered the name of user isn`t exist")

    def delete_user(self):
        indenificator = False
        while indenificator == False:
            username = input("username: ")
            try:
                auth.authenticator.delete_user(username)
                indenificator = True
            except auth.InvalidUsername:
                print("You entered the name of user isn`t exist")

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username
        if auth.authorizor.check_permission("admin", username) == True:
            self.admin_menu(username)
        elif auth.authorizor.check_permission("read_only", username) == True:
            menu.ReaderMenu().run()
        elif auth.authorizor.check_permission("write_read", username) == True:
            menu.WholeMenu().run()
        elif auth.authorizor.check_permission("no_permissions", username) == True:
            print("Still has no permissions")

    def admin_menu(self, username):
        print("Hello admin")
        try:
            answer = ""
            while True:
                print(
                    """
Please enter a command:
\tnotebook\tGo to notebook
\tchange\tChange users permissions
\tban\tBan user
\tlogout\tLog out
"""
                )
                answer = input("enter a command: ").lower()
                try:
                    func = self.admin_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            None

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print(
                    """
Please enter a command:
\tlogin\tLogin
\tcreate\tCreate new user
\tquit\tQuit
"""
                )
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for using our program")


interpretetor = Interaction()

if __name__ == "__main__":
    interpretetor.menu()
