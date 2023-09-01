from pandas import DataFrame


def calc_average(index: int, col_name: str, df: DataFrame, window: int = 3) -> float:
    """
    Compute the average of the previous 'window' non-zero values.
    """
    non_zero_values = df.loc[:index - 1, col_name][df[col_name] != 0][-window:].tolist()
    if not non_zero_values:
        return 0
    return sum(non_zero_values) / len(non_zero_values)


def replace_zeros(group: DataFrame, col_name: str) -> DataFrame:
    group[col_name] = group.apply(
        lambda row: calc_average(row.name, col_name, group) if row[col_name] == 0 else row[col_name], axis=1)
    return group
