import pandas as pd


def correct_cumulative(df):
    diff = df.diff()
    mask = diff < 0

    for idx, is_negative in mask.items():
        if is_negative:
            if idx == 0:  # If it's the first row of the group, just set it to zero or similar
                df.iloc[idx] = 0
            else:
                df.iloc[idx] = df.iloc[idx - 1]
    return df


def compute_avg_ratio(df):
    return df['Daily tests'].mean() / df['Daily cases'].mean()


def fill_na_based_on_ratio(row, avg_ratios):
    if pd.isna(row['Daily tests']):
        multiplier = row['Daily cases'] if row['Daily cases'] > 1 else 1
        return avg_ratios[row['Entity']] * multiplier
    return row['Daily tests']

# %%
