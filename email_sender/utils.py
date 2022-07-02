import pandas as pd


def csv_to_json(fp):
    """Parse contents in CSV file into JSON objects

    Args:
        fp (str): path to CSV file

    Returns:
        list[dict]: list of python dictionaries
    """
    return pd.read_csv(fp, keep_default_na=False).to_dict(orient='records')


def json_to_csv(obj_list, fp):
    """Save JSON objects into CSV file (format similar to customers.csv mentioned in the requirements)

    Args:
        obj_list (list[dict]): list of python dictionaries, each dictionary has keys ['TITLE', 'FIRST_NAME', 'LAST_NAME', 'EMAIL']
        fp (str): path to CSV file
    """
    columns = ['TITLE', 'FIRST_NAME', 'LAST_NAME', 'EMAIL']
    pd.DataFrame.from_dict(obj_list)[columns].to_csv(fp, index=False)
