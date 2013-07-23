from depict.model.class_ import Class_
from depict.model.method import Method

class TestClass():
    def test_creation(self):
        Class_('fake_class_name', 'fake_class_id')

    def test_add_one_method(self):
        class_ = Class_('dummy_class_name', 'dummy_class_id')
        method = Method('dummy_name', 'dummy_id', class_)
        class_.add_method(method)