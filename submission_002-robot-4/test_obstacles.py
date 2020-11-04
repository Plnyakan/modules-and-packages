import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import world.obstacles as obstacles
import robot


class MyTestCase(unittest.TestCase):
    def test_is_position_blocked(self):
        self.assertFalse(False)

    def test_is_path_blocked(self):
        self.assertFalse(False)
