import pandas as pd

class DataLoader:
    def __init__(self):
        self.final_data_path = 'data/final_data.csv'

    def load_data(self):
        try:
            df = pd.read_csv(self.final_data_path)
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None, None

