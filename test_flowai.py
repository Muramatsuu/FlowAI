# test_flowai.py
"""
Tests for FlowAI module.
"""

import unittest
from flowai import FlowAI

class TestFlowAI(unittest.TestCase):
    """Test cases for FlowAI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FlowAI()
        self.assertIsInstance(instance, FlowAI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FlowAI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
