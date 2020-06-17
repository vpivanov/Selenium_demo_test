import unittest
from Examples import Example


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This will run once before all methods")

    @classmethod
    def tearDownClass(cls):
        print("This will run once after every methods")

    def setUp(self):
        print("This will run before every method")

    def tearDown(self):
        print("This will run after every method")

    def test_add(self):
        result = Example.add(self, 10, 20)
        self.assertEqual(result, 30)

    def test_sub(self):
        result = Example.sub(self, 50, 30)
        self.assertEqual(result, 20)



if __name__ == '__main__':
   unittest.main()
