from langchain_core.tools import tool
import pandas as pd
from .financial_calculator import FinancialCalculator



@tool
def liquidity(company_name):
    """Provide liquidity trends and analysis for the given company(give the company name in Title Case)"""

    ratios= FinancialCalculator(company_name)
    liquidity_ratios = pd.DataFrame({
        'Current Ratio': ratios.current_ratio,
        'Quick Ratio': ratios.quick_ratio
    })
    return liquidity_ratios

@tool
def solvency(company_name):
    """Provide solvency trends and analysis for the given company(give the company name in Title Case)"""

    ratios= FinancialCalculator(company_name)
    solvency_ratios = pd.DataFrame({
        'Debt to Equity Ratio': ratios.debt_equity_ratio,
        'Debt to Assets Ratio': ratios.debt_assets_ratio
    })
    return solvency_ratios

@tool
def profitability(company_name):
    """Provide profitability trends and analysis for the given comapny(give the company name in Title Case)"""

    ratios= FinancialCalculator(company_name)
    profitability_ratios = pd.DataFrame({
        'Return on Assets (ROA)': ratios.return_assets,
        'Return on Equity (ROE)': ratios.return_equity
    })
    return profitability_ratios

@tool
def income_growth(company_name):
    """Provide income growth/contraction analysis for the given company(give the company name in Title Case) """
    metric= FinancialCalculator(company_name)
            
    return metric.income_pct_change