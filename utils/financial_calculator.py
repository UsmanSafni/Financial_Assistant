import pandas as pd
from .data_loader import DataLoader

class FinancialCalculator:
    def __init__(self,company_name):
        self.path_files = DataLoader()
        self.load_data(company_name)

    def load_data(self,company_name):
        # Load the data and initialize dataframes
        self.df = self.path_files.load_data()
        self.company_df = self.df[self.df['Company_name'] == company_name]
        # Convert relevant metrics to numeric
        self.extract_financial_metrics()
        
        self.income_pct_change = self.calculate_net_income_pct_change()
        self.ratios = self.calculate_ratios()

    def extract_financial_metrics(self):
        # Extract metrics
        self.current_assets = self.extract_metric('Total current assets')
        self.current_liabilities = self.extract_metric('Total current liabilities')
        self.inventories = self.extract_metric('Inventories')
        self.total_assets = self.extract_metric('Total assets')
        self.stockholders_equity = self.extract_metric('Total stockholders\' equity')
        self.total_liabilities = self.extract_metric('Total liabilities')
        self.net_income = self.extract_metric('Net income')

    def extract_metric(self, metric_name):
        return pd.to_numeric(self.company_df[self.company_df['Metric'] == metric_name].iloc[0, 1:], errors='coerce')

    

    def calculate_ratios(self):
        # Calculate ratios
        self.current_ratio = self.current_assets / self.current_liabilities
        self.quick_ratio = (self.current_assets - self.inventories) / self.current_liabilities
        self.debt_equity_ratio = self.total_liabilities / self.stockholders_equity
        self.debt_assets_ratio = self.total_liabilities / self.total_assets
        self.return_assets = self.net_income / self.total_assets
        self.return_equity = self.net_income / self.stockholders_equity

        self.ratios = pd.DataFrame({
            'Current Ratio': self.current_ratio,
            'Quick Ratio': self.quick_ratio,
            'Debt to Equity Ratio': self.debt_equity_ratio,
            'Debt to Assets Ratio': self.debt_assets_ratio,
            'Return on Assets (ROA)': self.return_assets,
            'Return on Equity (ROE)': self.return_equity,
            'Income Growth' : self.income_pct_change
        })
        return self.ratios

    def calculate_net_income_pct_change(self):
        # Extract Net Income row for the given company
        net_income_row = self.company_df[self.company_df['Metric'] == 'Net income']
        # Skip the 'Metric' and 'Company_name' columns, keeping only the years' data
        self.net_income = net_income_row.iloc[0, 1:-1] 
        # Convert Net Income to numeric
        self.net_income = pd.to_numeric(self.net_income, errors='coerce')
        # Calculate the year-over-year percentage change
        self.income_pct_change = self.net_income.pct_change() * 100  
        return self.income_pct_change


