import requests
from bs4 import BeautifulSoup


print("test requests")
# r = requests.get('https://api.github.com/events')
# r = requests.get('http://httpbin.org/get', proxies=dev_proxies)
# r = requests.get('https://api.github.com/events', proxies=dev_proxies)

r = requests.get('https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF', proxies=dev_proxies)
#
# r = requests.get('http://douban.com')

# print(r.text)

bsObj = BeautifulSoup(r.text, 'html5lib')
data_list = []
i = 0

for idx, tr in enumerate(bsObj.find_all('tr')):
    if idx != 0:
        tds = tr.find_all('td')
        print(type(tds))
        # data_list.append({'name':tds[1].string})
    # i= i+1
    # if i==10:
    #     break

print(data_list)

with open('./res.txt', 'wt') as f:
    f.write(r.text)
# print(r1.text)
