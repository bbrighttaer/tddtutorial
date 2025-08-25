import pytest
from src.calculator import Calculator

class TestCalculator: 
    
    def test_add_two_positive_numbers(self):
        """Test adding two positive numbers."""
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5