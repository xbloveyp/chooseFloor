from django.shortcuts import render

# Create your views here.
from choose.simulation import simulation


def index(request):
    randomNum, building_data, high_floor = simulation()
    building_data_view = []
    for i in range(len(building_data)):
        item = building_data[i]
        building_item_map = {}
        building_item = []
        for x in range(high_floor):
            unit_item_set = []
            building_floor_item = []
            for unit_item in item:
                for y in range(len(unit_item)):
                    room_item = unit_item[y]
                    if x == high_floor - 1 and y == 0:
                        unit_item_set.append(room_item[x-1]['unit'])
                    if x < len(room_item):
                        building_floor_item.append(room_item[x])
                    else:
                        building_floor_item.append({})
            building_item.append(building_floor_item)
        building_item_map["data"] = building_item
        building_item_map["unit"] = list(unit_item_set)
        building_item_map["building"] = i + 1
        building_data_view.append(building_item_map)
    return render(request, 'chooseFloor.html', {'building_data': list(building_data),'building_data_view':building_data_view, 'randomNum': str(randomNum)})
