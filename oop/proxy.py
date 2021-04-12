class File:

    def __init__(self, filename):

        self._filename = filename

    def load(self):

        print('Loading file... [{}]'.format(self._filename))

    def open(self):

        print('Opening file... [{}]'.format(self._filename))


class Proxy:

    def __init__(self, subject):

        self._subject = subject
        self.proxy_state = None

class ProxyFile(Proxy):

    def open(self):

        if self.proxy_state == None:
            self._subject.load()
            self._proxy_state = 1

        print('Opening file... [{}]'.format(self._subject._filename))


if __name__ == '__main__':
    
    proxy_file1 = ProxyFile(File('Big_File_1'))
    proxy_file2 = ProxyFile(File('Big_File_2'))

    proxy_file1.open() # Loading.
    proxy_file1.open() # Not loading.
    proxy_file2.open() # Loading.
    proxy_file2.open() # Not loading.
    proxy_file1.open() # Not loading. 