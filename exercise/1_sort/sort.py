import time
import random


def verify(in_arr):
    assert in_arr == sorted(in_arr)


def bubble_sort(in_arr):
    #  TODO 对in_arr原地排序, 通过测试
    return in_arr


if __name__ == '__main__':
    # 随机生成数组
    test_arr = list(range(1000))
    # 打乱数组
    random.shuffle(test_arr)

    time_start = time.process_time()  # 记录程序开始时间
    test_arr = bubble_sort(test_arr)
    print('cost:', time.process_time() - time_start)  # 计算排序的耗时

    # 验证
    verify(test_arr)
    print('pass')
