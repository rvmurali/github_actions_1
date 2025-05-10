"""
A simple calculator module for demonstrating pytest coverage
"""

class Calculator:
    """A simple calculator class with basic operations"""
    
    def add(self, a, b):
        """Add two numbers and return the result"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a and return the result"""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers and return the result"""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b and return the result
        
        Raises:
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """Calculate a raised to power b and return the result"""
        return a ** b
    
    def average(self, numbers):
        """Calculate the average of a list of numbers
        
        Args:
            numbers: List of numbers
            
        Returns:
            The average as a float, or 0 if the list is empty
        """
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    
    def factorial(self, n):
        """Calculate the factorial of n
        
        Args:
            n: A non-negative integer
            
        Returns:
            The factorial of n
            
        Raises:
            ValueError: If n is negative
        """
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)