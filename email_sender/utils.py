import pandas as pd


def csv_to_json(fp):
    """
    Convert initial CSV file to JSON
    """
    return pd.read_csv(fp).to_dict(orient='records')


def json_to_csv(obj, fp):
    """
    Convert JSON back to CSV file with original format
    """
    columns = ['TITLE', 'FIRST_NAME', 'LAST_NAME', 'EMAIL']
    return pd.DataFrame.from_dict(obj)[columns].to_csv(fp, index=False)
