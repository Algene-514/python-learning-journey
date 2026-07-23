from survey import AnonymousSurvey
sex = AnonymousSurvey('你的性别是什么')
print('按T键终止程序')
# 显示问题并存储答案
sex.ask()
while True:
    sex_ = str(input('输入性别'))
    if sex_ == "T":
        break
    sex.response(sex_)
sex.show_response()
print(sex.responses)