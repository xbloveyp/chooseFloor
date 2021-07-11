#!/usr/bin/env python
import random

def main():
    randomNum = random.randint(1, 320)
    building = [1, 2, 3, 4]
    unit = [[13, 12, 11], [10, 9, 8], [7], [6, 5]]
    room = [2,1]
    foor = {13:[2, 18], 12:[2, 18], 11:[1, 18], 10:[1, 18], 9:[1, 18], 8:[1, 18], 7:[1, 18], 6:[1, 18], 5:[1, 18]}
    foor_weight = {1:1,2:2,3:3,4:4,5:7,6:8,7:10,8:11,9:12,10:13,11:14,12:15,13:13,14:14,15:18,16:19,17:20,18:5}
    unit_weight = {13:12,12:14,11:16,10:10,9:18,8:20,7:8,6:6,5:4}
    building_data = []
    for i in range(len(building)):
        unit_item = unit[i]
        unit_data = []
        for j in range(len(unit_item)):
            room_data = []
            unit_num = unit_item[j]
            for k in range(len(room)):
                foor_data = []
                foor_set = foor.get(unit_num)
                start = foor_set[0]
                for l in range(foor_set[1] - foor_set[0] + 1):
                    foor_data.append(start + l)
                room_data.append(foor_data)
            unit_data.append(room_data)
        building_data.append(unit_data)
    a = random_weight(foor_weight)


def random_weight(weight_data):
    _total = sum(weight_data.values())    # 权重求和
    _random = random.uniform(0, _total)   # 在0与权重和之前获取一个随机数
    _curr_sum = 0
    _ret = None
    try:
        _keys = weight_data.iterkeys()    # 使用Python2.x中的iterkeys
    except AttributeError:
        _keys = weight_data.keys()        # 使用Python3.x中的keys
    for _k in _keys:
        _curr_sum += weight_data[_k]             # 在遍历中，累加当前权重值
        if _random <= _curr_sum:          # 当随机数<=当前权重和时，返回权重key
            _ret = _k
            break
    return _ret

if __name__ == '__main__':
    main()


