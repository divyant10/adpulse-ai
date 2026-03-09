import pandas as pd


def analyze_support(df):

    # normalize column names
    df.columns = df.columns.str.strip().str.lower()

    # top issues
    issue_counts = df["issue_type"].value_counts()

    # average resolution time
    avg_resolution = df["resolution_time"].mean()

    # priority distribution
    priority_counts = df["priority"].value_counts()

    report = {
        "Top Issues": issue_counts,
        "Average Resolution Time": avg_resolution,
        "Priority Distribution": priority_counts
    }

    return report