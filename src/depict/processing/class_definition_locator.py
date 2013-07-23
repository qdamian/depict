from depict.model.class_ import Class_
from depict.model.class_repo import GlobalClassRepo
from depict.collection.static.source_code_parser import GlobalSourceCodeParser

class ClassDefinitionLocator():
    def __init__(self, source_code_parser = GlobalSourceCodeParser, class_repo = GlobalClassRepo):
        self.source_code_parser = source_code_parser
        self.source_code_parser.register(self)
        self.class_repo = class_repo
    
    def process(self, file_name, src_code):
        self.source_code_parser.parse(file_name, src_code)
        
    def on_class(self, name, id_):
        self.class_repo.add(Class_(name, id_))
