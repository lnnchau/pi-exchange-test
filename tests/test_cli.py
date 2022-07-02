from pathlib import Path
from test_variables import CUSTOMERS_FP, CUSTOMERS_WITH_EMPTY_EMAIL_FP, EXPECTED_OUTPUT, TEMPLATE_FP, ERROR_FP
import subprocess
import json
import filecmp


def test_cli(tmp_path):
    command = ["python3", "cli.py", TEMPLATE_FP,
               CUSTOMERS_FP, tmp_path, tmp_path / 'errors.csv']
    subprocess.run(command)

    for output in EXPECTED_OUTPUT:
        recipient = output['to']
        expected_output_file = tmp_path / f'{recipient}.json'

        assert tmp_path.exists()
        assert expected_output_file.exists()

        email_obj = json.load(expected_output_file.open('r'))

        assert isinstance(email_obj, dict)
        assert email_obj == output

    assert Path(tmp_path / 'errors.csv').exists() is False


def test_cli_w_invalid_case(tmp_path):
    expected_error_file = tmp_path / 'errors.csv'
    command = ["python3", "cli.py", TEMPLATE_FP,
               CUSTOMERS_WITH_EMPTY_EMAIL_FP, tmp_path, expected_error_file]
    subprocess.run(command)

    for output in EXPECTED_OUTPUT:
        recipient = output['to']
        expected_output_file = tmp_path / f'{recipient}.json'

        assert tmp_path.exists()
        assert expected_output_file.exists()

        email_obj = json.load(expected_output_file.open('r'))

        assert isinstance(email_obj, dict)
        assert email_obj == output

    assert expected_error_file.exists()
    assert filecmp.cmp(str(expected_error_file), ERROR_FP)
