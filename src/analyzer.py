
import pandas as pd
import numpy as np

def monthly_summary(df: pd.DataFrame):
    return df.groupby("Month")["Amount"].sum()

def savings_ratio(df: pd.DataFrame):
    income = df[df["Type"] == "Income"].groupby("Month")["Amount"].sum()
    expenses = df[df["Type"] == "Expense"].groupby("Month")["Amount"].sum()
    ratio = (income - expenses) / income
    return pd.DataFrame({"Income": income, "Expenses": expenses, "SavingsRatio": ratio})

def detect_anomalies(df: pd.DataFrame, z_thresh=2):
    mean = df["Amount"].mean()
    std = df["Amount"].std()
    df["ZScore"] = (df["Amount"] - mean) / std
    anomalies = df[np.abs(df["ZScore"]) > z_thresh]
    return anomalies
