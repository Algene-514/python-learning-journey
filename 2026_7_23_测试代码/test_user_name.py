# 先导入模块
import unittest
from user_name import user

class NameTestCase(unittest.TestCase):
    '''测试user_name.py'''

    def test_first_last_name(self):
        formatted_name = user('al','gene')
        self.assertEqual(formatted_name, 'Al Gene')
    def test_last_middle_name(self):
        formatted_name = user('al','gene',"514")
        self.assertEqual(formatted_name, 'Al Gene 514')

if __name__ == '__main__':
    unittest.main()
# 注意！
'''
Python默认把根目录作为了工作默认途径。Python去根目录找不到本目录的文件，所以会FileNoFound
解决方法：右键该目录，将目录标记为源代码目录即可！
哎呀，这里卡了我好久！！！还是第一时间问AI吧！！！
'''

# 编写测试方法时必需以test打头，这样它才会再运行该文件时自动运行！！！
# 可以在TestCase类中使用很长的方法名且必需是描述性的，这样才能看懂测试未通过时输出的结果

# 1 测试类：
# 1.1 各种断言方法：
'''
assertEqual(a,b)                核实 a == b
assertNotEqual(a,b)             核实 a != b
assertTure(x)                   核实x为Ture
assertFalse(x)                  核实x为False
assertIn(item,list)             核实item在列表list中
assertNotIn(item,list)           核实item不在列表list中
'''
























