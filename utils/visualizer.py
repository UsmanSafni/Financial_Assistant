import matplotlib.pyplot as plt
from .financial_calculator import FinancialCalculator

def generate_plot(plot_type,company_name):
    metrics=FinancialCalculator(company_name)
    plt.figure(figsize=(10, 6))

    if plot_type == "Liquidity Ratios":
        metrics.ratios[['Current Ratio', 'Quick Ratio']].plot(marker='o')
        plt.title('Liquidity Ratios Trend (Current & Quick Ratios)')
        plt.ylabel('Ratio')

    elif plot_type == "Solvency Ratios":
        metrics.ratios[['Debt to Equity Ratio', 'Debt to Assets Ratio']].plot(marker='o')
        plt.title('Solvency Ratios Trend (Debt to Equity Ratio)')
        plt.ylabel('Ratio')

    elif plot_type == "Profitability Ratios":
        metrics.ratios[['Return on Assets (ROA)','Return on Equity (ROE)']].plot(marker='o')
        plt.title('Profitability Ratios Trend')
        plt.ylabel('Ratio')

    elif plot_type == "Income Growth":
        metrics.income_pct_change.plot( marker='o')
        plt.title('Income Growth/Contraction')
        plt.ylabel('Growth')



    plt.xlabel("Years")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    return plt
