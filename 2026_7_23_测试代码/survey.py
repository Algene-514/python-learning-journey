class AnonymousSurvey:
    '''收集匿名调查问卷的答案'''
    def __init__(self,question):
        self.question = question  #定义类中的变量
        self.responses = []

    def ask(self):
        '''显示调查问卷'''
        print(self.question)

    def response(self,answer):
        '''收集调查问卷的回答'''
        self.responses.append(answer)

    def show_response(self):
        '''显示所有调查的回答'''
        print("回答如下：")
        for answer in self.responses:
            print(answer)
if __name__ == '__main__':
    sex = AnonymousSurvey('你的性别是什么')
    sex.ask()
    sex.response()
    sex.show_response()
