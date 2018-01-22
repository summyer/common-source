#!/usr/bin/env python3
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


import unittest


class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

##另一种重要的断言就是期待抛出指定类型的Error，
##比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
##如果抛出的确实是KeyError就通过测试
##with self.assertRaises(KeyError):
##    value = d['empty']
        
if __name__ == '__main__':
    unittest.main()
    
