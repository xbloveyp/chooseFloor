import random

def simulation():
    randomNum = random.randint(1, 320)
    building = [1, 2, 3, 4]
    unit = [[13, 12, 11], [10, 9, 8], [7], [6, 5]]
    room = [2, 1]
    floor = {13: [2, 18], 12: [2, 18], 11: [1, 18], 10: [1, 18], 9: [1, 18], 8: [1, 18], 7: [1, 18], 6: [1, 18],
            5: [1, 18]}
    building_weight = {1: 10, 2: 10, 3: 2, 4: 1}
    unit_weight = [{13: 12, 12: 14, 11: 16}, {10: 10, 9: 18, 8: 20}, {7: 8}, {6: 6, 5: 4}]
    floor_weight = {1: 1, 2: 2, 3: 3, 4: 4, 5: 27, 6: 28, 7: 40, 8: 41, 9: 42, 10: 43, 11: 44, 12: 45, 13: 43, 14: 44,
                   15: 48, 16: 49, 17: 50, 18: 25}
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
                    floor_map["buildind"] = i + 1
                    floor_map["unit"] = unit_num
                    floor_map["room"] = k + 1
                    floor_map["floor_status"] = 1
                    floor_data.append(floor_map)
                floor_data = floor_data[::-1]
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
        floor_random = 18 - floor_random
        building_data[building_random - 1][unit_id][random.randint(0, 1)][floor_random]['floor_status'] = 2
    return randomNum, building_data

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
