import abc


# command interface
class Command(metaclass=abc.ABCMeta):
    def __init__(self, reciver):
        self.reciver = reciver

    @abc.abstractmethod
    def execute(self):
        pass


# concrete commands
class Login(Command):
    def execute(self):
        self.reciver.login()

class Logout(Command):
    def execute(self):
        self.reciver.logout()


# invoker
class Btn:
    def __init__(self, command):
        self.command = command

    def click(self):
        self.command.execute()


# reciver
class Db:
    def login(self):
        print('Welcome!')

    def logout(self):
        print('Good bye!')


if __name__ == '__main__':
    db = Db()

    loginCommand = Login(db)
    loginBtn = Btn(loginCommand)
    loginBtn.click()

    logoutCommand = Logout(db)
    logoutBtn = Btn(logoutCommand)
    logoutBtn.click()
