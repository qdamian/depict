import ast

class SourceCodeParser(ast.NodeVisitor):
    def __init__(self):
        self.class_id = None
        self.class_col_offset = 0

    def visit_ClassDef(self, node):
        id_ = self.file_name + ":" + str(node.lineno)
        self.class_id = id_
        self.class_col_offset = node.col_offset
        try:
            self.observer.on_class(node.name, id_)
        except AttributeError:
            pass
        return super(SourceCodeParser, self).generic_visit(node)
  
    def visit_FunctionDef(self, node):
        if node.col_offset <= self.class_col_offset:
            self.class_id = None
        id_ = self.file_name + ":" + str(node.lineno)
        try:
            self.observer.on_function(node.name, id_, self.class_id)
        except AttributeError:
            pass
        return super(SourceCodeParser, self).generic_visit(node)
          
    def generic_visit(self, node):
        return super(SourceCodeParser, self).generic_visit(node)
    
    def parse(self, file_name, src_file):
        '''Raises any exception that ast.visit raises.
           E.g. SyntaxError, IndentationError'''
        self.file_name = file_name
        content = str(src_file.read())
        root = ast.parse(content)
        return super(SourceCodeParser, self).visit(root)

    def register(self, observer):
        self.observer = observer
        
GlobalSourceCodeParser = SourceCodeParser()