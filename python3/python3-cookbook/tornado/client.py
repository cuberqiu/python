from tornado.httpclient import HTTPClient, AsyncHTTPClient
from tornado import gen
import requests
from flask import json
import os
import subprocess

# def synchronous_fetch(url):
#     http_client=HTTPClient()
#     response = http_client.fetch(url)
#     return response.body
#
# '''
# tornado 中推荐使用协程来实现异步代码
# 使用协程几乎像写同步代码一样简单, 并且不需要浪费额外的线程. 它们还通过减少上下文切换来 使并发编程更简单。
# '''
#
# @gen.corputine
# def fetch_coroutine(url):
#     http_client = AsyncHTTPClient()
#     response = yield http_client.fetch(url)
#     return response.body
#
# async def fetch_coroutine_same(url):
#     http_client = AsyncHTTPClient()
#     response = await http_client.fetch(url)
#     return response.body
cookies = """jupyterhub-hub-login="2|1:0|10:1541415130|20:jupyterhub-hub-login|44:ODNiNGRmNTczOWQyNDA2ZGIxMzIxNTY5MDA1ODBiYWI=|97d9e35f95524f3b835bff2925e27ed3aa345a2f39d78fb8da907a9f9606a431"; x_host_key=16463aa5472-6c40b21bc0f3b2ca7f2c834610ea1eb3a632305d; pgv_pvid=5693413262; pgv_pvi=361239552; pgv_si=s9529296896; x-host-key-oaback=164a686892f-51442e8c373fdf20fcfe42b68e5f9139560959a9; x-host-key-idcback=164b1b7d0d8-e5a743576b1d3b92840f5e1a76c45ad2cd7fdebf; ASSESS_PPE=shPi9qHreQmQVEvsWsKKSJUW7AbrmCAuVPfbiEv392zdqWvct3gpKBnRInT43kDAC5OldI9ytx7kUSGBvT%2b3kipxWglKvb%2fJ9jXLeaw4y9D8vGRedyID17vflNT4wniCNdJ3tr57k8LlmaUVfMLjMr%2b%2bN32GRJcOySAm3I0pSc5XHFoQx3ZqbmFt%2fVEU%2b1%2bs3yHykaQm1hHWOKkpIAhZEpouNGuiJH4lUBcWHPA3o5KBt1pZ5PtTB3ald5%2bNugQrWiB9YEaW0RhpoNvn6qxSRyeeW2BszDeWwJf%2bvphw%2b66axO7tKLH29b5GdvwHeNVW0SBihh5T4zz%2fwP%2fJgDi4rSpHxsO8cfyiy46QDIuM71u5OimCLjGcKO7qV583DbWx; Tencent.OA.MyWorkspace.MyOAV2=24C775D6D2E943C934C61004DCBB4FA4ED9F95A6DF6F66AE4D9526607D37BD215E441B825C3FE783B3772E64297555CD4C77A9CB56D53C2A1A3E548585A6CA2FB79EB29685D4E2A0D5495E75EAAF2CFD0E9129997ACC151B5C94D046231BD432EF27ABEFBCAAD5984035DDC3AA31FB6DA947C82DB00856CD83E240B575FF1E0E2F9553C5D692BA1919E548ADA0638641; pgv_info==undefined&ssid=s4763816359; t_u=100707182abb965a%7C45a8d14d63b93aec; t_uid=cuberqiu; OA_TCOA_TICKET=tof:67C342033ED014D02223FD00D429F77DD4355A926694C7801A1C66EB3CD5E04E7B5414F9EDD3E67FA71B5DB4FB82A332D0E71F32D8EC7833F48FEF3750E0AA06C1BCC561BFF5E6484021B398623FEBC02127D74D2FD28C6006BFBBCDC132F9AE65F6C883D5E6EEE9A99C8BF879F40A11FF7FA81C983BF6A2188953B535C990903A3E83CF82493D2CFFFCCFC02E0E0240764AC53EDAF1828988B6A1AC286B13642D74CA5B6A146814D7208D927480F35965A3B54CA91053B9; TCOA_TICKET=A5838BBEAB7688B45B76E8806F2855E14209C6E00B4CEE9199CE6E0ECDC03CB16710FD0D93B1AB38AD08433C8FF1F45918875B2942670380273FCF4DAFB98215F97BC77634092CB20E0C82BAB1313F3567A06242C9D23B9129C656B8F2DCFDAE0F6810A021412354FCF7EE8FF163B2C9BE4F6BC5B81A423E86AB86DFFA20FE321A8176334EE49FAD15B30BF34E1DF23F630C05F06005E5BC6D207D14A5EC01FA; TCOA=2QgoaWSpml; CAKEPHP=h6cla8c2g2u8t4jbcrt79s6bn1; RIO_TCOA_TICKET=tof:A5838BBEAB7688B4483BD5ABD74AB3F7823E39013593708E52A969385D9F6DFFD8A3817A0A5AFC4D723E1B43A3146D8F6F61185795B98F62D80F1568F609D4458B9AEB5B1DE1712F19669207E8B1DAC52ED51137F7CA44DB83A44D525CE88C2C717CC85F77CED2A6052BC7B2093D0256172FD010F699A9094254F25F3BD62D9864F91ECE090272573F213F986BF55EEB5CB3ABCBDCB4DFFA75566F2A6FC6B2314489290A7DD29BD4104922DE6827A5ABBFA6C44A750BEB52; jupyterhub-session-id=7da6002c95494276ab9592621c112ad8; _xsrf=2|10512ebc|1dfdbd96fdfd1a3407bfeadb84542d55|1541411508"""

def string_to_dict(arg):
    l = arg.split(";")
    # print(l)
    # print(len(l))
    ret = dict()
    for kw in l:
        kw = kw.strip()
        tmp = kw.split("=")
        if(len(tmp)==2):
            ret[tmp[0]] = tmp[1]

    return ret

# print(string_to_dict("x_host_key=16463aa5472-6c40b21bc0f3b2ca7f2c834610ea1eb3a632305d; pgv_pvid=5693413262;"))
# r=requests.get(url="http://127.0.0.1:8080/user/", cookies=string_to_dict(cookies))
# r=requests.get(url="http://127.0.0.1:8080/user/", cookies=cookies)
# r=requests.get(url="http://127.0.0.1:8080")
# print(r.text)


# payload = {"key":"has key"}
# headers = {"Content-Type":"application/json"}
#
# r = requests.post(url="http://localhost:8080/myform/", data=json.dumps(payload), headers=headers)
# # print(r.text)
#
# # r = requests.get(url="http://localhost:8080/", headers=headers)
#
# print(r.text)

x,s = subprocess.getstatusoutput("pip freeze")
print(s)
