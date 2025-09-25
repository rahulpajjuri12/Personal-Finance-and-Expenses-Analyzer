
from src.data_loader import load_data
from src.analyzer import monthly_summary, savings_ratio, detect_anomalies
from src.visualizer import plot_income_vs_expenses, plot_category_spending, plot_trend

# Load data
df = load_data("data/expenses.csv")


print("📊 Monthly Summary:\n", monthly_summary(df))
print("\n💰 Savings Ratio:\n", savings_ratio(df))
print("\n⚠️ Anomalies:\n", detect_anomalies(df))

# Visualization
plot_income_vs_expenses(savings_ratio(df))
plot_category_spending(df)
plot_trend(df)
