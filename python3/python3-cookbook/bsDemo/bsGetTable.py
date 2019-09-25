from bs4 import BeautifulSoup
import requests
import pandas as pd

dev_proxies = {'https': 'https://dev-proxy.oa.com:8080',
               'http': 'http://dev-proxy.oa.com:8080'}

r = requests.get('https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF', proxies=dev_proxies)
# print(type(r.text))


def paser_html(ht, file_name):
    soup = BeautifulSoup(ht, 'html5lib')
    th_name = []
    func = []

    tables = soup.find_all('table')

    print("table numbers :", len(tables))

    # tab = tables[0]
    i = 1
    with open(file_name, 'w') as f:
        for tab in tables:
            for th in tab.find_all('th'):
                # print(type(th.getText()))
                th_name.append(th.getText())

            if len(th_name) == 3 and "Name" in th_name[1]:
                print(th_name)
                for idex, tr in enumerate(tab.find_all('tr')):
                    if idex != 0:
                        td = tr.find_all('td')
                        # print(type(td))

                        # print(type(td[1].getText()))
                        f.write(td[1].getText() + '\n')
                        # print(func[0])
                        print(i)
                        i = i + 1

            th_name.clear()



import re
zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
def paser_html_hive(ht, file_name):
    soup = BeautifulSoup(ht, 'html5lib')
    uls = soup.find_all('ul')

    ul = uls[0]
    i = 1
    j = 1  # 710  41  669
    x = 1
    f = open(file_name, 'w')
    for li in ul.find_all('li'):
        for span in li.find_all('span'):
            func = span.getText()
            if i % 2 == 0 and not zh_pattern.search(func):
                # print(j, " ", span.getText())
                f.write(span.getText()+'\n')
                j = j+1
            i = i+1


apache_hive_file_name = "./func_list_hive2.txt"
tdw_hive_file_name = "./func_list_tdw_hive.txt"


def txt_2_excel(txt_file, xls_file):
    data = pd.read_table(txt_file)
    data.columns = list(range(data.shape[1]))
    data.to_excel(xls_file)


tdw_hive_udf_xls = "./tdw_hive_udf.xls"
hive2_udf_xls = "./hive2_udf.xls"
add_udf_txt = "./add_udf.txt"
add_udf_xls = "./add_udf.xls"
add_udf_des_xls = "./add_udf_des.xls"
add_udf_des_txt = "./add_udf_des.txt"
add_udf_type_txt = "./return_type.txt"
add_udf_type_xls = "./return_type.xls"


def pick_func(target, reference):
    tdw_hive = open(reference, 'r')
    tdw_udf = tdw_hive.read()
    add_udf_file = open(add_udf_txt, 'w')
    add_udf_file.write("add_udf\n")

    t = pd.read_excel(target)
    for hive_udf in t['hive2']:
        # print(i, " ", func)
        hive_udf_ = split_func(hive_udf)
        if hive_udf_ not in tdw_udf:
            add_udf_file.write(hive_udf+'\n')



def split_func(func):
    pattern = re.compile('\(')
    return re.split(pattern, func)[0]


def paser_html_description(ht, add_udf, add_udf_update):
    soup = BeautifulSoup(ht, 'html5lib')
    th_name = []

    tables = soup.find_all('table')

    func_dict = dict()

    print("table numbers :", len(tables))

    # tab = tables[0]
    i = 1
    for tab in tables:
        for th in tab.find_all('th'):
            # print(type(th.getText()))
            th_name.append(th.getText())

        if len(th_name) == 3 and "Name" in th_name[1]:
            print(th_name)
            for idex, tr in enumerate(tab.find_all('tr')):
                if idex != 0:
                    td = tr.find_all('td')

                    # f.write(td[2].getText() + '\n')
                    # func_dict[td[1].getText()] = td[2].getText()  # description
                    func_dict[td[1].getText()] = td[0].getText()  # return type

                    print(i)
                    i = i + 1

        th_name.clear()

    funcs = pd.read_excel(add_udf)
    f = open(add_udf_update,'w')
    print(funcs)
    for func in funcs['udf']:
        f.write(func_dict[func]+'\n')




if __name__ == "__main__":
    # txt_2_excel(tdw_hive_file_name, tdw_hive_udf_xls)
    # txt_2_excel(apache_hive_file_name, hive2_udf_xls)
    # paser_html(r.text, apache_hive_file_name)
    # all_text = open("./res.txt").read()
    # paser_html_hive(all_text, tdw_hive_file_name)

    # pick_func(hive2_udf_xls, tdw_hive_file_name)
    # txt_2_excel(add_udf_txt, add_udf_xls)

    #  get description
    # paser_html_description(r.text, add_udf_xls, add_udf_des_txt)
    # txt_2_excel(add_udf_des_txt, add_udf_des_xls)

    # get return type
    paser_html_description(r.text, add_udf_xls, add_udf_type_txt)
    txt_2_excel(add_udf_type_txt, add_udf_type_xls)


