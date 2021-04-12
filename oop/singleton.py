class Singleton:

    __instance = None

    @staticmethod
    def get_instance():

        if Singleton.__instance == None:
            Singleton()
        
        return Singleton.__instance

    def __init__(self):

        if Singleton.__instance != None:

            raise Exception("It's a singleton.")
        else:

            Singleton.__instance = self


if __name__ == "__main__":

    s = Singleton()
    print(s)

    s1 = Singleton()
    print(s1)

    s = Singleton.get_instance()
    print(s)

    s1 = Singleton.get_instance()
    print(s1)
