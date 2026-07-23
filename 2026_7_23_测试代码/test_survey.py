import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey类的测试'''
    def setUp(self):
        '''
        创建一个调查对象和一组答案，共使用的测试方法使用
        '''
        question = "你的性别是什么?"
        self.sex_survey = AnonymousSurvey(question) # 实例：my_survey
        self.ans= ['琪露诺','摸你莎','古明地恋']
    def test_store_single_response(self):
        '''测试单个能否正常保存'''
        self.sex_survey.response(self.ans[0])
        self.assertIn(self.ans[0],self.sex_survey.responses)
        # question = ('你的性别是什么')
        # my_survey = AnonymousSurvey(question)
        # my_survey.response("男")
        # self.assertIn("男",my_survey.responses)

    def test_store_multiple_response(self):
        for response in self.ans:
            self.sex_survey.response(response)
        for response in self.ans:
            self.assertIn(response,self.sex_survey.responses)

        '''测试多个能否正常保存'''
        # self.my_survey.response(self.anw)
        # question = ('你的性别是什么')
        # my_survey = AnonymousSurvey(question)
        # anw = [1,2,3,4,5]
        # my_survey.response(anw)
        # self.assertIn(anw, my_survey.responses)
        '''
        这里又重新定义了测试的类，太麻烦了
        下面用方法setUp来提高其效率，其让我们只创建对象一次，就能在每个测试方法中使用
        如果在TestCase类中包含了方法setUp(),Python将先运行它，再运行各个以test_打头的方法
        这样每个方法中都可以直接使用在方法setUp()中创建的对象
        # 但是搞完setUp好像跟之前变换有点大，因为只剩一个函数，更简单了
        '''



if __name__ == '__main__':
    unittest.main()





