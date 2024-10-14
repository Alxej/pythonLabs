import re
import matplotlib.pyplot as plt
import datetime
import collections


def create_time(date_str: str):
    time = datetime.time(hour=int(date_str[:2]),
                         minute=int(date_str[3:5]),
                         second=int(date_str[6:8]),
                         microsecond=int(date_str[9:12]))

    return time


def get_dictionary(input_path: str):
    with open(input_path, 'r') as f:
        lines = f.readlines()
        dictionary = {}
        for line in lines:
            if re.search(r'KEEP', line) is not None and re.search(r'A00000000001', line) is not None:  # noqa E501
                device_to_value_dict = {}
                capacitive_devices_string = re.findall(r'capacitive_devices=[[][\w][\d]+(?:,[\w][\d]+)+[]]|capacitive_devices=[[][\w\d+][]]', line) # noqa E501
                if len(capacitive_devices_string) > 0:
                    capacitive_devices = re.findall(r'[\w][\d]+', capacitive_devices_string[0]) # noqa E501
                values_string = re.findall(r'link_power_arr=[[][\d]+(?:,[\d]+)+[]]|link_power_arr=[[][\d]+[]]', line) # noqa E501
                if len(values_string) > 0:
                    values = re.findall(r'[\d]+', values_string[0])
                    for i in range(len(values)):
                        device_to_value_dict[capacitive_devices[i]] = int(values[i]) # noqa E501
                time = create_time(line[:12])
                dictionary[time] = device_to_value_dict
    return dictionary


def get_minutes_range(data: dict, start: int, minutes_count: int):
    bot_measure = datetime.time(14, start, 0, 0)
    top_measure = datetime.time(14, start + minutes_count, 0, 0)
    return {key: val for key, val in data.items() if key <= top_measure and key >= bot_measure} # noqa E501


def get_definite_data(data: dict, device_name: str):
    new_dict = {}
    for time in data.keys():
        if device_name in data[time].keys():
            new_dict[time] = data[time][device_name]
    return new_dict


def time_to_float(time: datetime.time):
    return time.hour + time.minute/60.0 + time.second/3600.0 + time.microsecond/3600000.0 # noqa E501


def get_device_names_set(data: dict):
    device_name_list = []
    for key in data.keys():
        for device_name in data[key].keys():
            device_name_list.append(device_name)

    return set(device_name_list)


def create_first_plot(data: dict):
    new_data = get_minutes_range(data=data, start=0, minutes_count=10)
    definited_data = get_definite_data(data=new_data,
                                       device_name="B00000000003")
    od = collections.OrderedDict(sorted(definited_data.items()))
    keys = [time_to_float(key) for key in od.keys()]
    values = od.values()
    plt.subplot(2, 1, 1)
    plt.plot(keys, values)
    plt.legend(["B00000000003"])


def create_second_plot(data: dict):
    new_data = get_minutes_range(data=data, start=5, minutes_count=5)
    device_name_set = get_device_names_set(data=new_data)
    plt.subplot(2, 1, 2)
    for device_name in device_name_set:
        defined_data = get_definite_data(data=new_data,
                                         device_name=device_name)
        od = collections.OrderedDict(sorted(defined_data.items()))
        keys = [time_to_float(key) for key in od.keys()]
        values = od.values()
        plt.plot(keys, values)
        plt.legend(list(device_name_set))


if __name__ == "__main__":
    data = get_dictionary(input_path='3/extra/n_log1.txt')
    create_first_plot(data=data)
    # 3
    create_second_plot(data=data)
    plt.show()
