class AbstractHandler(object):
    
    def __init__(self, nxt):

        self._nxt = nxt

    def handle(self, req):

        handled = self.processRequest(req)

        if not handled:
            self._nxt.handle(req)

    def processRequest(self):

        raise NotImplementedError('')


class MainHandler(AbstractHandler):

    def processRequest(self, req):

        if req == 0:
            print('Class: {}, Request: {}'.format(self.__class__.__name__, req))
            return True


class SecondaryHandler(AbstractHandler):

    def processRequest(self, req):

        if req == 1:
            print('Class: {}, Request: {}'.format(self.__class__.__name__, req))
            return True    


class LastHandler(AbstractHandler):

    def processRequest(self, req):

        if req == 2:
            print('Class: {}, Request: {}'.format(self.__class__.__name__, req))
            return True    

class DefaultHandler(AbstractHandler):

    def processRequest(self, req):
        
        print('Class: {}, Request: {}'.format(self.__class__.__name__, req))
        return True    


class User:

    def __init__(self):
        initial = None

        self.handler = MainHandler(SecondaryHandler(LastHandler(DefaultHandler(initial))))

    def agent(self, user_request): 
  
        for request in user_request: 
            self.handler.handle(request) 


if __name__ == "__main__": 
    user = User()

    l = [0, 1, 2, 3]

    user.agent(l)

"""
Output:
Class: MainHandler, Request: 0
Class: SecondaryHandler, Request: 1
Class: LastHandler, Request: 2
Class: DefaultHandler, Request: 3
"""