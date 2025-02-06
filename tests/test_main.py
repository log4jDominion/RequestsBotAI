import unittest
from main import say_hello

class TestMain(unittest.TestCase):

    def testSayHello(self):
        expected = "hello world"
        actual = say_hello()
        self.assertEqual(expected, actual)