import uuid
import datetime


class Logger:

    def text(self): pass

    def severity(self): pass     

    def id(self):

        return str(uuid.uuid4())

    def date_time(self):

        return datetime.datetime.now()

    def register(self, msg):

        self.ID = self.id()
        self.msg = self.text(msg)
        self.sev = self.severity()
        self.date = self.date_time()

    def __str__(self):

        return str.format("{}, Severity: {}, Created: {}, ID: {}", \
            self.msg, self.sev, self.date, self.ID)



class Critical(Logger):

    #@override
    def text(self, t):

        return 'Critical Event: ' + t

    def severity(self):

        return 1

    
class Error(Logger):
    
    #@override
    def text(self, t):

        return 'Error: ' + t

    def severity(self):

        return 1
    

class UserRegistered(Logger):
    
    #@override
    def text(self, t):

        return 'User created, user id: [{}]' . format(t)

    def severity(self):

        return 10


if __name__ == '__main__':

    event0 = Critical()
    event0.register('DB unreachable')
    print(event0)

    event1 = Error()
    event1.register('Buffer overflow')
    print(event1)

    event2 = UserRegistered()
    event2.register('12345678')
    print(event2)

"""
Output:
Critical Event: DB unreachable, Severity: 1, Created: 2020-08-29 07:43:45.683662, ID: 178ede30-02c1-4108-b57b-6af1dd89968d
Error: Buffer overflow, Severity: 1, Created: 2020-08-29 07:43:45.683792, ID: 0077cc7e-1217-4d3e-a013-5dbeb6c542c5
User created, user id: [12345678], Severity: 10, Created: 2020-08-29 07:43:45.683865, ID: 503304dc-7a9e-4876-8846-4576ceae9d56
"""