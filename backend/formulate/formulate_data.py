
import pandas as pd
from backend.formulate.config_parser import Parser
from backend.utilities.constants import DF_TYPE_COLUMNS, FORMAT, EXPORT_FILENAME
from backend.utilities.utility import get_folder_path

class FormulateData(object):

    def __init__(self):
        self.parser = Parser()
        month_map = self.parser.get_month_map()
        self.monthly_expenses = dict()
        self.formulate(month_map)
        self.export_to_csv()

    def getattr(self):
        return self.monthly_expenses

    def formulate(self, month_map):
        for type in DF_TYPE_COLUMNS:
            for month in month_map[FORMAT][type]:
                self.monthly_expenses.update({month: self.formulate_df(month_map[month], type)})

    def formulate_df(self, df, type):
        new_df = df.copy()
        new_df.drop_duplicates(inplace=True)
        if type == 'Manual':
            return self.formulate_txt(new_df)
        if type == 'Type 2':
            return self.formulate_type2(new_df)
        new_df = new_df[DF_TYPE_COLUMNS[type]]
        new_df.dropna(how='all', inplace=True)
        return new_df

    def formulate_txt(self, df):
        col_name = df.columns[0]
        df['Description'] = df[col_name].str.replace(' - ', ' ')
        df[['Description', 'Amount', 'Date']] = df[col_name].str.extract(r'(.*) - (\d+)(\(\d+/\d+\))?')
        df['Date'] = df['Date'].str.replace('(', '').str.replace(')', '')
        df['Amount'] = pd.to_numeric(df['Amount'])
        df.drop(col_name, axis=1, inplace=True)
        df.dropna(how='all', inplace=True)
        return df
    
    def formulate_type2(self, df):
        df = df[DF_TYPE_COLUMNS['Type 2']]
        df['amount'] = df['amount'].abs()
        df.dropna(how='all', inplace=True)
        return df
    
    def export_to_csv(self):
        with pd.ExcelWriter(get_folder_path(EXPORT_FILENAME), engine='xlsxwriter') as writer:
            for month in self.monthly_expenses:
                self.monthly_expenses[month].to_excel(writer, sheet_name=month)
