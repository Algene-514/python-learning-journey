# 等比数列求和工具
def geometric_sum(first_term,common_ratio,term_number):
    try:
        if term_number <= 0:
            raise ValueError("项数必须大于0")
        total = 0
        for i in range(term_number):
            total += first_term*common_ratio**i
        return total
    except TypeError:
            raise TypeError(' 所有参数必须是数字类型')
# 列表总和计算
def sum_list(list0):
    total = 0
    for i in list0:
        total +=i
    return total

if __name__ == "__main__":
    # 自动化测试
    try:
        assert geometric_sum(2, 2, 3) == 14,"┗|｀O′|┛ 嗷~~"
        assert sum_list([1, 2, 3]) == 6,'┗|｀O′|┛ 嗷~~'
        print("✅ 所有测试通过，代码功能良好")
    except AssertionError:
        print("❌ 测试失败，代码需要维护")