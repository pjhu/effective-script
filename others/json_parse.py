import json


def read_es():
    with open('2.json', encoding='utf-8') as json_data:
        data = json.load(json_data)
    rst = []
    for d in data["buckets"]:
        rst.append(d["key"])
    print(len(rst))
    return rst


def read_store():
    with open('store.log', encoding='utf-8') as store:
        data = store.read()
    data_list = data.split('\n')
    return data_list


def compare(start, end):
    es = read_es()
    store = read_store()
    print(store[end-1])
    print(set(store[start: end]) - set(es))
    print(len(set(store[start: end]) - set(es)))
    print(set(es) - set(store[start: end]))

if __name__ == '__main__':
    compare(0, 1172)
