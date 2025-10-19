# test_nodeutility.py
"""
Tests for NodeUtility module.
"""

import unittest
from nodeutility import NodeUtility

class TestNodeUtility(unittest.TestCase):
    """Test cases for NodeUtility class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeUtility()
        self.assertIsInstance(instance, NodeUtility)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeUtility()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
