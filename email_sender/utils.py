import imp
import pandas as pd


def csv_to_dict(fp):
    """
    Convert initial CSV file to python dictionary
    """
    return pd.read_csv(fp).to_dict(oriend='records')


def dict_to_csv(obj, fp):
    """
    Convert python dictionary back to CSV file with original format
    """
    columns = ['TITLE', 'FIRST_NAME', 'LAST_NAME', 'EMAIL']
    return pd.DataFrame.from_dict(obj)[columns].to_csv(fp, index=False)
