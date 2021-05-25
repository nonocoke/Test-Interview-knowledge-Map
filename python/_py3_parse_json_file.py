#coding:utf8
#! /usr/bin/python3
import json
import sys

# python3 _py3_parse_json_file.py pv_2021052010_052012.log
def test():
    # Reading data back
    with open('data.json', 'r') as f:
        data = json.load(f)
        print(data)

    # Writing JSON data
    with open('data.json', 'w') as f:
        json.dump(data, f)


def get_pv_lost(file_name):
    d = {} # 一个普通的字典
    _file_name = file_name
    with open("./%s" % _file_name,'r') as load_f:
        load_dict = json.load(load_f)
        # print(load_dict["data"])
    d = {}
    for data in load_dict["data"]:
        # d.setdefault(str(data["dimensions"][1]["value"]), []).append(1)
        key = str(data["dimensions"][1]["value"])
        if key not in d:
            d[key] = []
        init = 0
        for half_of_hour in data["data"]:
            if half_of_hour[1] is None or half_of_hour[1] == "null":
                continue
            init += int(str(half_of_hour[1]))
        d[key] = init
        # print(type(data["dimensions"][1]["value"]), )
        # print(data["data"])
        # print('----')
    print(d)
    all_pv = sum(d.values())
    lost_pv = all_pv - d["200"] - d["206"]
    print("{}/{} = {:0.2}%".format(lost_pv, all_pv, lost_pv*1.0/all_pv*100))


if __name__ == "__main__":
    print(sys.argv[1])
    get_pv_lost(sys.argv[1])