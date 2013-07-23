class Repo(object):
    def __init__(self):
        self.elements = {}
    
    def add(self, element):
        '''
        The element is expected to have an id_ attribute
        '''
        self.elements[element.id_] = element
    
    def get(self, id_):
        try:
            return self.elements[id_]
        except KeyError:
            return None