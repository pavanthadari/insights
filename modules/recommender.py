import pandas as pd
import numpy as np

def generate_recommendations(df):
    strategies = []
    kpis       = []
    correlations = {}
    impact     = []
    automation = []

    # 1) Identify numeric columns
    num_cols = df.select_dtypes(include='number').columns.tolist()

    # 2) Example: Sales KPIs (if present)
    if 'sales' in num_cols:
        total_sales = df['sales'].sum()
        avg_sales   = df['sales'].mean()
        # assume a datetime index or column named 'date'
        if 'date' in df.columns:
            monthly = df.set_index('date').resample('M')['sales'].sum()
            growth = monthly.pct_change().iloc[-1]
            kpis.append(f"Total Sales: {total_sales:.2f}")
            kpis.append(f"Avg Monthly Sales: {monthly.mean():.2f}")
            kpis.append(f"Latest M-on-M Growth: {growth:.1%}")
            # 3) Strategy based on trend
            if growth < 0:
                strategies.append("Launch targeted promotions to reverse declining sales")
            else:
                strategies.append("Increase inventory to meet rising sales demand")

    # 4) Correlation matrix (only strong ones)
    corr = df[num_cols].corr().abs()
    for i in corr.columns:
        for j in corr.columns:
            if i!=j and corr.at[i,j] > 0.7:
                correlations[f"{i}↔{j}"] = corr.at[i,j]

    # 5) Impact summary
    if correlations:
        # pick top pair
        pair, val = max(correlations.items(), key=lambda x: x[1])
        impact.append(f"High correlation ({val:.2f}) between {pair.replace('↔',' and ')}—one may drive the other.")

    # 6) Automation ideas
    if 'sales' in num_cols and 'date' in df.columns:
        automation.append("Automate monthly sales reports and anomaly alerts for >10% deviation")

    return strategies, kpis, correlations, impact, automation
