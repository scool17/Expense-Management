import configparser
import pandas as pd
import os

NumToMonth = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"}

SHEETS = 'Sheets'
CSV = 'CSV'
TEXT = 'Text'

class Parser(configparser.ConfigParser):
    def __init__(self):
        super().__init__()
        self.read('backend/fileInfo.ini')
        self.month_map = {'type': []}
        self.trip_map = dict()
        self.folder_path = self.get('Global', 'folderPath')
        self.update_month_map()
        self.update_trip_map()

    def get_options(self, section):
        return self.options(section)
    
    def get_filename(self, section, option):
        return self.get(section, option)

    def update_month_map(self):
        self.parse_sheets()
        self.parse_csv()
        self.parse_txt()


    def update_trip_map(self):
        pass

    def parse_sheets(self):
        sheets = self.get_options(SHEETS)
        sheet_months, sheet_year = sheets[0].split('_')
        sheet_start_month, sheet_end_month = sheet_months.split('-')
        for i in range(int(sheet_start_month), int(sheet_end_month) + 1):
            self.month_map[NumToMonth[i] + '_' + sheet_year] = get_dataframe(read_excel, (self.folder_path.strip('"') + '/' + self.get_filename(SHEETS, sheets[0]).strip('"')), NumToMonth[i])
            self.month_map['type'].append({NumToMonth[i] + '_' + sheet_year: 'excel'})


    def parse_csv(self):
        csv = self.get_options(CSV)
        types = list()
        files = list()
        for i in csv:
            if 'type' in i.split('_'):
                types.append(i)
            else:
                files.append(i)
        for i in files:
            month, year = i.split('_')
            self.month_map[NumToMonth[int(month)] + '_' + year] = get_dataframe(read_csv, (self.folder_path.strip('"') + '/' + self.get_filename(CSV, i).strip('"')))
            self.month_map['type'].append({NumToMonth[int(month)] + '_' + year: self.get(CSV, (i+'_type')).strip('"')})


    def parse_txt(self):
        text = self.get_options(TEXT)
        for i in text:
            month, year = i.split('_')
            self.month_map[NumToMonth[int(month)] + '_' + year] = get_dataframe(read_txt, (self.folder_path.strip('"') + '/' + self.get_filename(TEXT, i).strip('"')))
            self.month_map['type'].append({NumToMonth[int(month)] + '_' + year: 'manual'})


def get_dataframe(function_name, file_path, sheet_name=None):
    return function_name(file_path, sheet_name)

def read_csv(file_path, sheet_name=None):
    return pd.read_csv(file_path)

def read_excel(file_path, sheet_name):
    xls = pd.ExcelFile(file_path)
    return pd.read_excel(xls, sheet_name)

def read_txt(file_path, sheet_name=None):
    return pd.read_csv(file_path)

# def parse_string(csv):
#     csv_items = list()
#     for i in csv:
#         if '-' in i:
#             num, suffix = i.split('_', 1)
#             for j in num.split('-'):
#                 csv_items.append((j) + '_' + suffix)
#         else:
#             csv_items.append(i)