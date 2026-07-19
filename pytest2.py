def calculate(a,b,c):
    print("这是等比数列逻辑性求和工具")
    Sum = 0
    if  c <= 0  :
        print("项数不能小于等于0！")
    else:
        for i in range(0,c):
            Sum += a * b**i
        return Sum
if __name__ == "__main__":
    result = calculate(1,2,3)
    print(f'首项为1，公比为2且项数为3的测试结果是{result}')