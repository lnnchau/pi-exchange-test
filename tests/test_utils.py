from email_sender.utils import json_to_csv, csv_to_json
from test_variables import CUSTOMERS, CUSTOMERS_FP, CUSTOMER_WITH_EMPTY_EMAIL, CUSTOMERS_WITH_EMPTY_EMAIL_FP
import filecmp


def test_json_to_csv(tmp_path):
    csv_fp = tmp_path / 'customers.csv'
    json_to_csv(CUSTOMERS, str(csv_fp))

    assert filecmp.cmp(csv_fp, CUSTOMERS_FP)


def test_csv_to_json():
    customer_obj = csv_to_json(CUSTOMERS_FP)
    assert customer_obj == CUSTOMERS


def test_csv_to_json_w_invalid_case():
    customer_obj = csv_to_json(CUSTOMERS_WITH_EMPTY_EMAIL_FP)
    assert customer_obj == CUSTOMERS + [CUSTOMER_WITH_EMPTY_EMAIL]