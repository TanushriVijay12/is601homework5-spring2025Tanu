from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand

@pytest.fixture
def setup_calculations():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('7'), AddCommand()))
    Calculations.add_calculation(Calculation(Decimal('30'), Decimal('5'), SubtractCommand()))

def test_add_calculation(setup_calculations):
    calc = Calculation(Decimal('3'), Decimal('2'), AddCommand)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    latest = Calculations.get_latest()
    assert latest.a == Decimal('30') and latest.b == Decimal('5'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"

    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"
