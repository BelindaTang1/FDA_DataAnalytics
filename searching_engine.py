import pandas as pd
import os
import numpy as np
import datetime as dt

abs_path = os.path.abspath('')

data_file_list = ["pmnlstmn.txt", "pmn96cur.txt",
                  "pmn9195.txt", "pmn8690.txt", "pmn8185.txt", "pmn7680.txt"]
data_list = []

for i in range(len(data_file_list)):
    path = os.path.join(abs_path, "FDA Registration Record",
                        "510k", data_file_list[i])
    data_list.append(pd.read_csv(path, sep="|", encoding="cp1252"))
DATA = pd.concat(data_list)
DATA = DATA.reset_index(drop=True)
FDA_INFO_510K = DATA[['KNUMBER', 'APPLICANT', "COUNTRY_CODE", "DATERECEIVED",
                      'DECISIONDATE', "DECISION", 'PRODUCTCODE', "STATEORSUMM", "THIRDPARTY", 'DEVICENAME']]
FDA_INFO_510K = FDA_INFO_510K.rename(
    {'APPLICANT': 'MANUFACTURER', "DEVICENAME": "MODELNAME"}, axis="columns")
FDA_INFO_510K = FDA_INFO_510K.replace(np.nan, "NA", regex=True)
FDA_INFO_510K['DATERECEIVED'] = pd.to_datetime(
    FDA_INFO_510K['DATERECEIVED'], errors="coerce")
FDA_INFO_510K['DECISIONDATE'] = pd.to_datetime(
    FDA_INFO_510K['DECISIONDATE'], errors="coerce")


class search_filter(object):
    def __init__(self, df, knumber=None, manufacturer=None, countryCode=None, dateReceived=None, decisionDate=None, decision=None, productCode=None, stateOrSum=None, thirdParty=None, ModelName=None):
        self.knumber = knumber
        self.manufacturer = manufacturer
        self.countryCode = countryCode
        self.dateReceived = dateReceived
        self.decsionDate = decisionDate
        self.decision = decision

    def filter_510k_kNumber(
        self, df, knumber): return df[df["KNUMBER"].str.lower() == knumber.lower()]

    def filter_510k_manufacturer(df, manufacturer): return df[df["MANUFACTURER"].str.lower(
    ).str.contains(manufacturer.lower())]

    def filter_510k_countryCode(
        df, countryCode): return df[df["COUNTRY_CODE"].str.lower() == countryCode.lower()]

    def filter_510k_dateReceived(df, year_mode):
        if year_mode[1] == 'before':
            result_df = df[df["DATERECEIVED"].dt.year < year_mode[0]]
        elif year_mode[1] == "in":
            result_df = df[df["DATERECEIVED"].dt.year == year_mode[0]]
        else:
            result_df = df[df["DATERECEIVED"].dt.year > year_mode[0]]
        return result_df

    def filter_510k_decisionDate(df, year_mode):
        if year_mode[1] == 'before':
            result_df = df[df["DECISIONDATE"].dt.year < year_mode[0]]
        elif year_mode[1] == "in":
            result_df = df[df["DECISIONDATE"].dt.year == year_mode[0]]
        else:
            result_df = df[df["DECISIONDATE"].dt.year > year_mode[0]]
        return result_df

    def filter_510k_decision(
        df, decision): return df[df["DECISION"].str.lower() == decision.lower()]

    def filter_510k_productCode(
        df, productCode): return df[df["PRODUCTCODE"].str.lower() == productCode.lower()]

    def filter_510k_stateOrSum(
        df, stateOrSum): return df[df["STATEORSUMM"].str.lower() == stateOrSum.lower()]
    def filter_510k_thirdParty(
        df, thirdParty): return df[df["THIRDPARTY"].str.lower() == thirdParty.lower()]

    def filter_510k_modelName(df, modelName): return df[df["MODELNAME"].str.lower(
    ).str.contains(modelName.lower())]


func_list = [filter_510k_kNumber, filter_510k_manufacturer, filter_510k_countryCode, filter_510k_dateReceived, filter_510k_decisionDate,
             filter_510k_decision, filter_510k_productCode, filter_510k_stateOrSum, filter_510k_thirdParty, filter_510k_modelName]
