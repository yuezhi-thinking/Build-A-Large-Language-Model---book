import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_one_plus_one(self):
        self.assertEqual(add(1, 1), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
