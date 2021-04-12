'''
    Model module.
'''
class User:

    def __init__(self, user_name = None, password = None):

        self. user_name = user_name
        self.password = password

    def credentials(self):

        return 'Name: {}, Password: {}'.format(\
            self.user_name, self.password)

    def get_all(self):

        return [
            User('Peter', 'password123'),
            User('Niels', 'password123'),
            User('Jacob', 'password123'),
            User('Bob', 'password123'),
        ]


'''
    View module.
'''
def start_view():

    print('MVC - a simple example.')


def show_all_users_view(l):

    print('Currently registered users:')

    for item in l:
        print(item.credentials())


def end_view():

    print('Exiting...')


'''
    Control module.
'''
def start():

    start_view()
    show_all()
    end_view()


def show_all():

    users = User().get_all()

    return show_all_users_view(users)


if __name__ == "__main__":

   start()