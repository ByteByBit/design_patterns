class Message(object):

    msg = ''

    def get_msg(self):

        return self.msg


class Error(Message):

    msg = 'Error '


class Warning(Message):

    msg = 'Warning '


class Notify(Message):

    msg = 'Notify '


class MessageFactory():

    def create(self, msg_type):

        target = msg_type.capitalize()
        return globals()[target]()


if __name__ == '__main__':
    
    msg = MessageFactory()
    types = ['Error', 'Warning', 'Notify']
    for t in types:
        elem = msg.create(t).get_msg()
        print(elem)