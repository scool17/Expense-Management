import configparser
import pandas as pd

class Parser(configparser.ConfigParser):
    def __init__(self):
        super().__init__()
        self.read('fileInfo.ini')

    def get_file_info(self, month, parse_type):
        pass

    def parse_sheets(self):
        pass

    def parse_csv(self):
        pass

    def parse_txt(self):
        pass

    def get_dataframe(function_name, file_path, sheet_name=None):
        return function_name(file_path, sheet_name)
    
    @staticmethod
    def read_csv(file_path, sheet_name=None):
        return pd.read_csv(file_path)
    
    @staticmethod
    def read_excel(file_path, sheet_name):
        xls = pd.ExcelFile(file_path)
        return pd.read_excel(xls, sheet_name)
    
    @staticmethod
    def read_txt(file_path, sheet_name=None):
        return pd.read_csv(file_path)