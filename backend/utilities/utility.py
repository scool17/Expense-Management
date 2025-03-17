import pandas as pd
import os
from dotenv import load_dotenv
from backend.utilities.constants import EXPORT_FILENAME

def get_dataframe(function_name, file_path, sheet_name=None):
    return function_name(file_path, sheet_name)

def read_csv(file_path, sheet_name=None):
    return pd.read_csv(file_path)

def read_excel(file_path, sheet_name=None):
    xls = pd.ExcelFile(file_path)
    return pd.read_excel(xls, sheet_name)

def read_txt(file_path, sheet_name=None):
    return pd.read_csv(file_path)

def get_folder_path(key):
    load_dotenv()
    env_var = os.getenv(key)
    return env_var

def load_data():
    return read_excel(get_folder_path(EXPORT_FILENAME))