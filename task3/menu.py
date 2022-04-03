import notebook
import auth_driver


class ReaderMenu:
    def __init__(self):
        self.notebook = notebook.notebook

        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.logout
        }

    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Logout
        """)

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo))

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def logout(self):
        print("Thank you for using your notebook today.")
        auth_driver.interpretetor.menu()


class WholeMenu(ReaderMenu):
    '''Display a menu and respond to choices when run.'''

    def __init__(self):
        self.notebook = notebook.notebook

        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.logout
        }

    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Log out
        """)

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        id = input("Enter a note id: ")

        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)


class AdminMenu(WholeMenu):
    def __init__(self):
        self.notebook = notebook.notebook

        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.go_to_admin_menu,
            "6": self.logout
        }

    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Admin Menu
        6. Logout
        """)

    def go_to_admin_menu(self):
        auth_driver.interpretetor.admin_menu()


if __name__ == "__main__":
    WholeMenu().run()
