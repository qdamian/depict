from depict.model.function import Function

class Method(Function):
    def __init__(self, name, id_, Class_):
        self.name = name
        self.id_ = id_
        self.Class_ = Class_
        
    def __repr__(self):
        return 'Method, name: ' + self.name + ', ID: ' + str(self.id_)