import pandas as pd


def txt_2_excel(txt_file, xls_file):
    data = pd.read_table(txt_file)
    # data.columns = list(range(data.shape[1]))
    data.to_excel(xls_file)


txt_file = "./test.txt"
xls_file = "./test.xls"

# txt_2_excel(txt_file, xls_file)

t = pd.read_excel(xls_file)
# print(t.head())
x = t[t["from"] == 102]["props"]

print(type(x))
print(x)

# for from_ in t["from"]:
#     if from_ == 102:
#         print(from_)