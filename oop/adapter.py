class CDMedia:

    def standard(self): pass

    def diameter(self): pass

    def data_density(self) :pass


class FlashMedia:

    def encode_type(self): pass

    def width(self): pass

    def height(self): pass

    def data_density(self) :pass


class Media(CDMedia):

    def encode_type(self):

        return 'IEC 60908'

    def diameter(self):

        return 12 # cm.

    def data_density(self):

        return '0.9 Gbit/in^2'


class Adapter(FlashMedia):

    def __init__(self, media):

        self.media = media

    def encode_type(self):

        return 'ONFI'

    def width(self):

        return 5 # cm.
    
    def height(self):

        return 2 # cm.

    def data_density(self):
        return '1.19 Tbits/in^2'


class USBPort:

    def __init__(self, media):

        self.__media = media

    def read_media(self):

        if self.__media.width() > 5 or \
           self.__media.height() > 2:

            raise Exception('USB port broken.')
        else:
            print('Reading...')


if __name__ == "__main__":

    media = Media()
    adapter = Adapter(media)
    port = USBPort(adapter)
    port.read_media()