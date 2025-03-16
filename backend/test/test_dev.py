

from backend.formulate.formulate_data import FormulateData
from backend.formulate.config_parser import Parser
import pandas as pd

folder_path = "/mnt/c/users/shubh/onedrive/PersonalProjects/ExpenseTracker/DataDump"
file_name = "June 2024.txt"

if __name__ == "__main__":
    fd = FormulateData()
    p = Parser()

    # file_path = folder_path + "/" + file_name
    # print(file_path)

    # df = pd.read_csv(file_path)
    # print(df)
    print(fd.getattr())
    # print(fd.monthly_expenses['June_2024'])