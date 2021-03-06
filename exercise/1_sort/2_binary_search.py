import time
import random
from . import sort


def binary_search(in_arr, target):
    #  TODO 第二题, 在排好序的数组中, 找到目标值的下标, 如[1,2,3,4,5,6], 找3, 则返回2, 因为in_arr[2] == 3
    return 0


if __name__ == '__main__':
    # 随机生成数组
    size = 1000
    test_arr = list(range(size))
    to_find = test_arr[random.randint(0, size - 1)]
    # 打乱数组
    random.shuffle(test_arr)

    test_arr = sort.bubble_sort(test_arr)
    # 验证排序结果
    assert test_arr == sorted(test_arr)

    time_start = time.process_time()  # 记录程序开始时间
    idx = binary_search(test_arr, to_find)
    print('cost:', time.process_time() - time_start)  # 计算查找的耗时

    # 验证
    assert test_arr[idx] == to_find

    print('pass')
