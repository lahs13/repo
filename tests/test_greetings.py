import unittest
from src.greetings import hello

class TestGreetings(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello('World'), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
