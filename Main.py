from Main_Interface import Menu_Interface

class Main:

    def __init__(self):
        self.menu = Menu_Interface()

    def showMenu(self):
        self.menu.run()

            


if __name__ == "__main__":
    main = Main()
    main.showMenu()