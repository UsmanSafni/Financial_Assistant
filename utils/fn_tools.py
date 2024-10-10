from langchain_core.tools import tool
import pandas as pd
from .financial_calculator import FinancialCalculator

#s= FinancialCalculator()

@tool
def liquidity(company_name):
    """Provide liquidity trends and analysis for the given company(give the company name in Title Case)"""

    s= FinancialCalculator(company_name)
# Combine into a single DataFrame for plotting
    liquidity_ratios = pd.DataFrame({
        #'Year/Quarter': years_quarters,
        'Current Ratio': s.current_ratio,
        'Quick Ratio': s.quick_ratio
    })


    return liquidity_ratios

@tool
def solvency(company_name):
    """Provide solvency trends and analysis for the given company(give the company name in Title Case)"""

    s= FinancialCalculator(company_name)
# Combine into a single DataFrame for plotting
    solvency_ratios = pd.DataFrame({
        #'Year/Quarter': years_quarters,
        'Debt to Equity Ratio': s.debt_equity_ratio,
        'Debt to Assets Ratio': s.debt_assets_ratio
    })
    return solvency_ratios

@tool
def profitability(company_name):
    """Provide profitability trends and analysis for the given comapny(give the company name in Title Case)"""

    s= FinancialCalculator(company_name)
# Combine into a single DataFrame for plotting
    profitability_ratios = pd.DataFrame({
        #'Year/Quarter': years_quarters,
        'Return on Assets (ROA)': s.return_assets,
        'Return on Equity (ROE)': s.return_equity
    })
    return profitability_ratios

@tool
def income_growth(company_name):
    """Provide revenue growth/contaction analysis for the given company(give the company name in Title Case) """
    s= FinancialCalculator(company_name)
            
    return s.income_pct_change