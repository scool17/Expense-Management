
import pandas as pd


class FormulateData(object):

    def __init__(self):
        pass

    def formulate_csv(df):
        pass

    def formulate_sheet(df):
        pass

    def formulate_txt(self, df, file_path, sheet_name):
        FormulateData.read_txt(file_path)
        df[['Description', 'Cost_Date']] = df['April expenses'].str.split("-", expand=True)
        df[["Cost", "Date"]] = df['Cost_Date'].str.split("(", expand=True)
