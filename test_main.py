import unittest
from main import is_even

class TestIsEven(unittest.TestCase):
    
    def test_even_numbers(self):
        """Test that is_even returns True for even numbers"""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(100))
        self.assertTrue(is_even(0))  # Zero is considered an even number
    
    def test_odd_numbers(self):
        """Test that is_even returns False for odd numbers"""
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(99))
    
    def test_negative_numbers(self):
        """Test that is_even works correctly with negative numbers"""
        self.assertTrue(is_even(-2))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(-1))
        self.assertFalse(is_even(-3))

if __name__ == '__main__':
    unittest.main()