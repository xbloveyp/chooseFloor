import random

# building = [1, 2, 3, 4]
# unit = [[13, 12, 11], [10, 9, 8], [7], [6, 5]]
# room = [2, 1]
# floor = {13: [2, 18], 12: [2, 18], 11: [1, 18], 10: [1, 18], 9: [1, 18], 8: [1, 18], 7: [1, 18], 6: [1, 18],
#          5: [1, 18]}
# building_weight = {1: 10, 2: 10, 3: 1, 4: 1}
# unit_weight = [{13: 12, 12: 14, 11: 16}, {10: 10, 9: 18, 8: 20}, {7: 8}, {6: 6, 5: 4}]
# floor_weight = {1: 1, 2: 2, 3: 3, 4: 4, 5: 27, 6: 28, 7: 30, 8: 31, 9: 32, 10: 33, 11: 34, 12: 35, 13: 33, 14: 34,
#                 15: 38, 16: 39, 17: 30, 18: 25}

building = [1, 2, 3, 4, 5, 6, 7]
unit = [[1, 2, 3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16, 17]]
room = [2, 1]
floor = {1: [1, 14], 2: [1, 14], 3: [1, 14], 4: [1, 14], 5: [1, 14], 6: [1, 14], 7: [1, 14], 8: [1, 14], 9: [1, 14],
         10: [1, 14], 11: [1, 14], 12: [1, 14]
    , 13: [1, 14], 14: [1, 14], 15: [1, 14], 16: [1, 14], 17: [1, 14]}
building_weight = {1: 5, 2: 1, 3: 4, 4: 1, 5: 1, 6: 1, 7: 1}
unit_weight = [{1: 10, 2: 10, 3: 10, 4: 10}, {5: 10, 6: 10}, {7: 10, 8: 10}, {9: 10, 10: 10}, {11: 10, 12: 10},
               {13: 10, 14: 10}, {15: 10, 16: 10, 17: 10}]
floor_weight = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 20, 8: 25, 9: 27, 10: 30, 11: 34, 12: 35, 13: 40, 14: 22}
high_floor = 14

def simulation(request):
    max_num = 476
    if bool(request.POST):
        setting_floor = request.POST['floor']
        if setting_floor is not None:
            if int(setting_floor) > max_num:
                randomNum = max_num
            else:
                randomNum = int(setting_floor)
    else:
        randomNum = random.randint(1, max_num)
    # randomNum = 310
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
        while True:
            result = set_building(building_data)
            if result == 1:
                break;
    return randomNum, building_data, high_floor


def set_building(building_data):
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
    floor_random = high_floor - floor_random
    room_num = random.randint(0, 1)
    if building_data[building_random - 1][unit_id][room_num][floor_random]['floor_status'] == 1:
        building_data[building_random - 1][unit_id][room_num][floor_random]['floor_status'] = 2
        return 1
    else:
        return 0


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
