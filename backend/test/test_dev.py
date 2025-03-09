

from backend.formulate.formulate_data import FormulateData

if __name__ == "__main__":
    fd = FormulateData()
    folder_path = "/mnt/c/users/shubh/onedrive/PersonalProjects/ExpenseTracker/DataDump"

     
    file_name = "July To Dec 2023.xlsx"
    file_path = folder_path + "/" + file_name
    print(file_path)
    df = fd.read_excel(file_path, "Jul")
    print(df)
