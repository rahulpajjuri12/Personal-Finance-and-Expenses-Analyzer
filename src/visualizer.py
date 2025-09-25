
import matplotlib.pyplot as plt

def plot_income_vs_expenses(summary_df):
    summary_df[["Income","Expenses"]].plot(kind="bar", figsize=(8,5))
    plt.title("Monthly Income vs Expenses")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()

def plot_category_spending(df):
    cat = df[df["Type"]=="Expense"].groupby("Category")["Amount"].sum()
    cat.plot(kind="pie", autopct='%1.1f%%', figsize=(6,6))
    plt.title("Category-wise Spending")
    plt.show()

def plot_trend(df):
    monthly = df.groupby("Month")["Amount"].sum()
    monthly.plot(kind="line", marker="o", figsize=(8,5))
    plt.title("Trend of Transactions Over Time")
    plt.ylabel("Amount")
    plt.show()
