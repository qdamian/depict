from depict.model.function import Function
from depict.model.method import Method
from depict.model.class_repo import GlobalClassRepo
from depict.model.function_repo import GlobalFunctionRepo
from depict.collection.static.source_code_parser import GlobalSourceCodeParser

class FunctionDefinitionLocator():
    def __init__(self, source_code_parser = GlobalSourceCodeParser, function_repo = GlobalFunctionRepo):
        self.source_code_parser = source_code_parser
        self.source_code_parser.register(self)
        self.function_repo = function_repo
    
    def process(self, file_name, src_code):
        self.source_code_parser.parse(file_name, src_code)
        
    def on_function(self, name, id_, class_id):
        if class_id:
            Class_ = GlobalClassRepo.get(class_id)
            _function_ = Method(name, id_, Class_)
        else:
            _function_ = Function(name, id_) 
        self.function_repo.add(_function_)
