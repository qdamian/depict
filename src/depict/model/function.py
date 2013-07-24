# pylint: disable=R0903
class Function(object):
    def __init__(self, name, id_):
        self.name = name
        self.id_ = id_

    def __eq__(self, other):
        return other.id_ == self.id_ 