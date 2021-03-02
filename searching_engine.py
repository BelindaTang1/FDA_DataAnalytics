import pandas as pd
import os

abs_path = os.path.abspath("")

data_file_list = ["pmnlstmn.txt", "pmn96cur.txt", "pmn9195.txt", "pmn8690.txt", "pmn8185.txt", "pmn7680.txt"]
data_list = []
for i in range(len(data_file_list)):
    path = os.path.join(abs_path, "FDA Registration Record", "510k", data_file_list[i])
    data_list.append(pd.read_csv(path, sep= "|", encoding="cp1252"))

DATA = pd.concat(data_list)





print(DATA.columns)