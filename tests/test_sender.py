
from email_sender.sender import EmailSenderViaFile
from test_data import TEMPLATE, CUSTOMERS, EXPECTED_OUTPUT, CUSTOMER_WITH_EMPTY_EMAIL, ERROR_FP
import json
import filecmp


def test_sender(tmp_path):
    sender = EmailSenderViaFile(
        TEMPLATE, CUSTOMERS, tmp_path, tmp_path / 'errors.csv')
    sender.send_email()

    for output in EXPECTED_OUTPUT:
        recipient = output['to']
        expected_output_file = tmp_path / f'{recipient}.json'

        assert tmp_path.exists()
        assert expected_output_file.exists()

        email_obj = json.load(expected_output_file.open('r'))

        assert isinstance(email_obj, dict)
        assert email_obj == output


def test_sender_with_empty_email(tmp_path):
    expected_error_file = tmp_path / 'errors.csv'

    sender = EmailSenderViaFile(
        TEMPLATE, CUSTOMERS + [CUSTOMER_WITH_EMPTY_EMAIL], tmp_path, expected_error_file)
    sender.send_email()

    # check if emails for valid customers are sent
    for output in EXPECTED_OUTPUT:
        recipient = output['to']
        expected_output_file = tmp_path / f'{recipient}.json'

        assert tmp_path.exists()
        assert expected_output_file.exists()

        email_obj = json.load(expected_output_file.open('r'))

        assert isinstance(email_obj, dict)
        assert email_obj == output

    # check if email for invalid customer is not sent
    invalid_recipient = CUSTOMER_WITH_EMPTY_EMAIL['EMAIL']
    invalid_output_file = tmp_path / f'{invalid_recipient}.json'

    assert invalid_output_file.exists() is False

    assert expected_error_file.exists()
    assert filecmp.cmp(str(expected_error_file), ERROR_FP)
