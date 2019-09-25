import csv

datas = [
    ['key1', 'value1'],
    ['key2', 'value2'],
    ['key3', 'value3']
]

datas1 = [
        {
            "degrees": [
                {
                    "_degree": 2,
                    "direction": "out",
                    "from": "102",
                    "label": "friends"
                }
            ],
            "results": [
                {
                    "_timestamp": 111,
                    "cacheRemain": -12,
                    "direction": "out",
                    "from": "102",
                    "label": "friends",
                    "props": {
                        "_count": -1,
                        "_timestamp": 111
                    },
                    "score": 1,
                    "timestamp": 111,
                    "to": "203"
                },
                {
                    "_timestamp": 111,
                    "cacheRemain": -12,
                    "direction": "out",
                    "from": "102",
                    "label": "friends",
                    "props": {
                        "_count": -1,
                        "_timestamp": 111
                    },
                    "score": 1,
                    "timestamp": 111,
                    "to": "202"
                }
            ],
            "size": 2
        }
    ]

# with open('./sample.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#
#     for row in datas:
#         writer.writerow(row)

    # writer.writerow(datas)

ret_data ={
    "degrees": [
        {
            "_degree": 2,
            "direction": "out",
            "from": "102",
            "label": "friends"
        }
    ],
    "results": [
        {
            "_timestamp": 111,
            "cacheRemain": -10,
            "direction": "out",
            "from": "102",
            "label": "friends",
            "props": {
                "_count": -1,
                "_timestamp": 111
            },
            "score": 1,
            "timestamp": 111,
            "to": "203"
        },
        {
            "_timestamp": 111,
            "cacheRemain": -11,
            "direction": "out",
            "from": "102",
            "label": "friends",
            "props": {
                "_count": -1,
                "_timestamp": 111
            },
            "score": 1,
            "timestamp": 111,
            "to": "202"
        }
    ],
    "size": 2
}


def get_graph_structure(dic_arg):

    results = dic_arg["results"]

    for result in results:
        result.pop("_timestamp")
        result.pop("cacheRemain")
        result.pop("props")
        result.pop("score")
        result.pop("timestamp")

    return dic_arg


print(get_graph_structure(ret_data))





