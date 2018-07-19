import abc, datetime


# interface for real subject
class DbInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connect(self):
        pass


# real subject...some db for example
class Db(DbInterface):
    def connect(self):
        return 'Connected'



# proxy which is logging and protecting
class ProxyDb(DbInterface):
    def __init__(self, real_subject, user):
        self.subject = real_subject
        self.user = user
        self.logger = {}

    def connect(self):
        if self.isAdmin():
            self.addLog('access granted')
            return self.subject.connect()
        else:
            self.addLog('access denied')
            return '[Connection error: permission denied]'

    def isAdmin(self):
        if self.user == 'Jhon':
            return True
        else:
            return False

    def addLog(self, log):
        self.logger[datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')] = log



# client
def app(subject):
    print(subject.connect())

if __name__ == '__main__':
    print('Without proxy:')
    subject = Db()
    app(subject)

    print()
    print('With proxy:')
    proxy = ProxyDb(subject, 'Jhon')
    app(proxy)
    print(proxy.logger)