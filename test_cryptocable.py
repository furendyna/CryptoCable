# test_cryptocable.py
"""
Tests for CryptoCable module.
"""

import unittest
from cryptocable import CryptoCable

class TestCryptoCable(unittest.TestCase):
    """Test cases for CryptoCable class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoCable()
        self.assertIsInstance(instance, CryptoCable)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoCable()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
