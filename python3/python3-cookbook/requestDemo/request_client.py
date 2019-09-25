import requests
# import json
from flask import jsonify, json

url = "http://127.0.0.1:5000/messages/"
# url = "http://10.241.106.212:80/graphs/getEdges"


# print(r.text)


# url = "http://10.241.106.212:80/graphs/getEdges"

headers = {"Content-Type": "application/json;charset=utf-8"}

kwargs= {
    "srcVertices": [
        {
            "serviceName": "KakaoFavorites",
            "columnName": "userName",
            "id": "102"
        }
    ],
    "steps": [
        {
            "step": [
                {
                    "label": "friends",
                    "direction": "out",
                    "offset": 0,
                    "limit": 10,
                    "duplicate": "raw"
                }
            ]
        }
    ]
}

kwdata =  {
	"v1":[{
    "srcVertices": [
        {
            "serviceName": "KakaoFavorites",
            "columnName": "userName",
            "id": "102"
        }
    ],
    "steps": [
        {
            "step": [
                {
                    "label": "friends",
                    "direction": "out",
                    "offset": 0,
                    "limit": 10,
                    "duplicate": "raw"
                }
            ]
        }
    ]
}]
,
"v2": [{
    "srcVertices": [
        {
            "serviceName": "KakaoFavorites",
            "columnName": "userName",
            "id": "102"
        }
    ],
    "steps": [
        {
            "step": [
                {
                    "label": "friends",
                    "direction": "out",
                    "offset": 0,
                    "limit": 10,
                    "duplicate": "raw"
                }
            ]
        }
    ]
}]
}
#


def get_one_graph(kwargs):
    url = "http://10.241.106.212:80/graphs/getEdges"

    headers = {"Content-Type": "application/json;charset=utf-8"}
    r = requests.post(url, data=json.dumps(kwargs), headers=headers)

    d = json.loads(r.text)

    print(r.text)
    print(type(d))
    print(d)


def get_graph_result(kwargs):
    """
    :param kwargs:  dict
    :return: dict
    """
    # TODO : put url in the conf file
    url = "http://10.241.106.212:80/graphs/getEdges"

    headers = {"Content-Type": "application/json;charset=utf-8"}

    ret_body = dict()

    for keys in kwargs:
        data = kwargs[keys][0]
        print(type(data))
        r = requests.post(url, data=json.dumps(data), headers=headers)
        graph_dict = json.loads(r.text)
        ret_body[keys] = [graph_dict]

    return ret_body



if __name__ == "__main__":
    # get_one_graph(kwargs)
    ret_graph = get_graph_result(kwdata)
    print(type(ret_graph))
    print(ret_graph)