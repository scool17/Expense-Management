import pandas as pd
from backend.utilities.utility import load_data

class Calculation:
    def __init__(self):
        self.data = load_data()


    def calculate(self, df):
        return
    
    def get_data(self):

        # print(len(self.data))
        # print(self.data.keys())
        total_sum = 0
        for key in list(self.data.keys())[9:]:
            sum = self.data.get(key)['Amount'].sum()
            print(key, sum)
            total_sum += sum
            # print(self.data.get(key)[self.data.get(key)['Description'].str.contains('Gas')])
            # print(self.data.get(key)[self.data.get(key)['Description'].str.contains('Gas')])
        print(total_sum)
        return self.data