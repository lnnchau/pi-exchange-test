from email_sender.utils import json_to_csv, csv_to_json
from test_data import CUSTOMERS, CUSTOMERS_FP
import filecmp


def test_json_to_csv(tmp_path):
    csv_fp = tmp_path / 'customers.csv'
    json_to_csv(CUSTOMERS, str(csv_fp))

    assert filecmp.cmp(csv_fp, CUSTOMERS_FP)


def test_csv_to_json():
    customer_obj = csv_to_json(CUSTOMERS_FP)
    assert customer_obj == CUSTOMERS
