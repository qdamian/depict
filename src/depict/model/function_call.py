from depict.model.function_repo import GlobalFunctionRepo

class FunctionCall():
    def __init__(self, function_id):
        self.function_id = function_id

    @property
    def function(self):
        return GlobalFunctionRepo.get(self.function_id)

    def __eq__(self, other):
        return self.function_id == other.function_id
    
    def __repr__(self):
        return 'ID: ' + self.function_id