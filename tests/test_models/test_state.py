#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests state"""
    def setUp(self):
        self.test_state = State
    def test_state(self):
        self.assertIs(self.test_state.name, '')

if __name__ == '__main__':
    TestState().unittest()
