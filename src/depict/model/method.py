from depict.model.function import Function

# pylint: disable=C0103, R0903
class Method(Function):
    def __init__(self, name, id_, Class_):
        super(Method, self).__init__(name, id_)
        self.Class_ = Class_
        
    def __repr__(self):
        return 'Method, name: ' + self.name + ', ID: ' + str(self.id_)