import unittest

f = lambda x : x**2

class SomeTest(unittest.TestCase):

    def test1(self):
        for i in range(100):
            self.assertEqual(f(i), i*i)

    def test2(self):
        for i in range(50):
            self.assertEqual(f(i + 1), i**3)

if __name__ == '__main__':
    unittest.main()
