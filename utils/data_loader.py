import pandas as pd

class DataLoader:
    def __init__(self):
        self.final_data_path = 'data/final_data.csv'
        #self.income_statement_path = 'data/income_final.csv'

    def load_data(self):
        try:
            df = pd.read_csv(self.final_data_path)
            #income_df = pd.read_csv(self.income_statement_path)
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None, None

