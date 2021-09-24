#!/usr/bin/env python
import random


def main():
    randomNum = random.randint(1, 466)
    building = [1, 2, 3, 4, 5, 6, 7]
    unit = [[1, 2, 3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16, 17]]
    room = [2, 1]
    floor = {1: [1, 14], 2: [1, 14], 3: [1, 14], 4: [1, 14], 5: [1, 14], 6: [1, 14], 7: [1, 14], 8: [1, 14], 9: [1, 14], 10: [1, 14], 11: [1, 14], 12: [1, 14]
             , 13: [1, 14], 14: [1, 14], 15: [1, 14], 16: [1, 14], 17: [1, 14]}
    building_weight = {1: 5, 2: 1, 3: 4, 4: 1, 5: 1, 6: 1, 7: 1}
    unit_weight = [{1: 10, 2: 10, 3: 10, 4: 10}, {5: 10, 6: 10}, {7: 10, 8: 10}, {9: 10, 10: 10}, {11: 10, 12: 10}, {13: 10, 14: 10}, {15: 10, 16: 10, 17: 10}]
    floor_weight = {1: 1, 2: 2, 3: 3, 4: 4, 5: 7, 6: 8, 7: 10, 8: 11, 9: 12, 10: 13, 11: 14, 12: 15, 13: 20, 14: 14}
    building_data = []
    for i in range(len(building)):
        unit_item = unit[i]
        unit_data = []
        for j in range(len(unit_item)):
            room_data = []
            unit_num = unit_item[j]
            for k in range(len(room)):
                floor_data = []
                floor_set = floor.get(unit_num)
                start = floor_set[0]
                for l in range(floor_set[1] - floor_set[0] + 1):
                    floor_map = {}
                    floor_map["id"] = start + l
                    floor_map["buildind"] = i
                    floor_map["unit"] = j
                    floor_map["status"] = 1
                    floor_data.append(floor_map)
                room_data.append(floor_data)
            unit_data.append(room_data)
        building_data.append(unit_data)
    for x in range(randomNum):
        building_random = random_weight(building_weight)
        building_units = unit[building_random - 1]
        unit_weight_item = unit_weight[building_random - 1]
        unit_random = random_weight(unit_weight_item);
        unit_id = 0
        for y in range(len(building_units)):
            if unit_random == building_units[y]:
                unit_id = y
                break
        floor_start = floor[unit_random][0]
        floor_random = random_weight(floor_weight)
        while floor_random == 1 and floor_start == 2:
            floor_random = random_weight(floor_weight)
        if floor_start == 2:
            floor_random -= 1
        building_data[building_random - 1][unit_id][random.randint(0, 1)][floor_random - 1]['status'] = 2
    print(building_data)

def random_weight(weight_data):
    _total = sum(weight_data.values())  # 权重求和
    _random = random.uniform(0, _total)  # 在0与权重和之前获取一个随机数
    _curr_sum = 0
    _ret = None
    try:
        _keys = weight_data.iterkeys()  # 使用Python2.x中的iterkeys
    except AttributeError:
        _keys = weight_data.keys()  # 使用Python3.x中的keys
    for _k in _keys:
        _curr_sum += weight_data[_k]  # 在遍历中，累加当前权重值
        if _random <= _curr_sum:  # 当随机数<=当前权重和时，返回权重key
            _ret = _k
            break
    return _ret


if __name__ == '__main__':
    main()
