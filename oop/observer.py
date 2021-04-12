import threading
import time


class Loader(threading.Thread):

    count = 5

    def load(self):

        if self.count < 1:
            return
        
        self.count -=  1
        time.sleep(1)

        print('Loading.')
        self.load()


class Worker(threading.Thread):

    count = 5

    def load(self):

        if self.count < 1:
            return
        
        self.count -=  1
        time.sleep(1)

        print('Worker running {}'.format(self.count))
        self.load()


if __name__ == '__main__':

    loader = Loader()
    loader.load()

    time.sleep(1)

    worker1 = Worker()
    worker1.load()

    worker2 = Worker()
    worker2.load()

    worker3 = Worker()
    worker3.load()