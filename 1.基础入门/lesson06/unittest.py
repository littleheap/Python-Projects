import unittest


class MyDict(dict):
    pass


class TestMyDict(unittest.TestCase):
    def setUp(self):
        print('测试前准备')

    def tearDown(self):
        print('测试后清理')

    def test_init(self):
        md = MyDict(one=1, two=2)
        self.assertEqual(md['one'], 1)
        self.assertEqual(md['two'], 2)
        # self.assertEqual(md['two'], 3)

    def test_nothing(self):
        pass


if __name__ == '__main__':
    unittest.main()

# python test_module.py
# python -m unittest test_module
# python -m unittest test_module.test_class
# python -m unittest test_module.test_class.test_method
