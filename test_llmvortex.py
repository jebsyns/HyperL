# test_llmvortex.py
"""
Tests for LLMVortex module.
"""

import unittest
from llmvortex import LLMVortex

class TestLLMVortex(unittest.TestCase):
    """Test cases for LLMVortex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LLMVortex()
        self.assertIsInstance(instance, LLMVortex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LLMVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
