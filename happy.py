import unittest

def get_name():
    name = 'HAPPY'
    return name

class MyTest(unittest.TestCase):

    def test_name_equal(self):
        self.assertEqual(get_name(), 'HAPPY')

if __name__ == '__main__':
    unittest.main()