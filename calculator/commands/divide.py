from decimal import Decimal
from calculator.commands.command import Command

class DivideCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
