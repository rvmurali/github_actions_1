"""
Test cases for the calculator module
"""
import pytest
from calculator.calculator import Calculator


class TestCalculator:
    """Test the Calculator class functionality"""
    
    @pytest.fixture
    def calculator(self):
        """Fixture to create a Calculator instance for tests"""
        return Calculator()
    
    def test_add(self, calculator):
        """Test the add method with various inputs"""
        assert calculator.add(1, 2) == 3
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0
        assert calculator.add(-1, -1) == -2
        assert calculator.add(0.1, 0.2) == pytest.approx(0.3)  # Handle floating point precision
    
    def test_subtract(self, calculator):
        """Test the subtract method with various inputs"""
        assert calculator.subtract(3, 2) == 1
        assert calculator.subtract(1, 1) == 0
        assert calculator.subtract(0, 1) == -1
        assert calculator.subtract(-1, -1) == 0
    
    def test_multiply(self, calculator):
        """Test the multiply method with various inputs"""
        assert calculator.multiply(2, 3) == 6
        assert calculator.multiply(0, 5) == 0
        assert calculator.multiply(-1, 5) == -5
        assert calculator.multiply(-2, -3) == 6
    
    def test_divide(self, calculator):
        """Test the divide method with various inputs"""
        assert calculator.divide(6, 3) == 2
        assert calculator.divide(5, 2) == 2.5
        assert calculator.divide(-6, 3) == -2
        assert calculator.divide(0, 5) == 0
    
    def test_divide_by_zero(self, calculator):
        """Test that dividing by zero raises the correct exception"""
        with pytest.raises(ZeroDivisionError):
            calculator.divide(5, 0)
    
    def test_power(self, calculator):
        """Test the power method with various inputs"""
        assert calculator.power(2, 3) == 8
        assert calculator.power(5, 0) == 1
        assert calculator.power(0, 5) == 0
        assert calculator.power(2, -1) == 0.5
    
    @pytest.mark.parametrize("numbers, expected", [
        ([1, 2, 3, 4, 5], 3.0),
        ([0, 0, 0], 0.0),
        ([-1, 0, 1], 0.0),
        ([], 0.0),  # Test empty list
    ])
    def test_average(self, calculator, numbers, expected):
        """Test the average method with various inputs using parameterization"""
        assert calculator.average(numbers) == expected
    
    def test_factorial_positive(self, calculator):
        """Test factorial with positive inputs"""
        assert calculator.factorial(0) == 1
        assert calculator.factorial(1) == 1
        assert calculator.factorial(5) == 120
    
    def test_factorial_negative(self, calculator):
        """Test factorial with negative inputs raises ValueError"""
        with pytest.raises(ValueError):
            calculator.factorial(-1)
    
    def test_factorial_type_error(self, calculator):
        """Test factorial with non-integer inputs raises TypeError"""
        with pytest.raises(TypeError):
            calculator.factorial(2.5)
    
    @pytest.mark.skip(reason="Example of skipped test for demonstration")
    def test_skipped_example(self, calculator):
        """This test is skipped on purpose to demonstrate skipped tests in the report"""
        assert False
    
    @pytest.mark.xfail(reason="Example of test expected to fail for demonstration")
    def test_xfail_example(self, calculator):
        """This test is expected to fail to demonstrate xfail tests in the report"""
        # This will fail intentionally to show failures in the report
        assert calculator.add(1, 1) == 3