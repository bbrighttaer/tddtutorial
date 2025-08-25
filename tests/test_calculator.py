import pytest
from src.calculator import Calculator

class TestCalculator: 
    
    def test_add_two_positive_numbers(self):
        """Test adding two positive numbers."""
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5
    
    def test_subtract_two_positive_numbers(self):
        """Test subtracting two positive numbers."""
        calc = Calculator()
        result = calc.subtract(3, 2)
        assert result == 1