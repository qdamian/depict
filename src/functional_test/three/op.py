class Addition:
    def __init__(self, operand_a, operand_b):
        self.result = operand_a.value + operand_b.value

    def __repr__(self):
        return str(self.result)
