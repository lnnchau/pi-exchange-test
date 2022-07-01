
from email_sender.sender import EmailSenderViaFile
from test_data import TEMPLATE, CUSTOMERS, EXPECTED_OUTPUT
import json


def test_sender(tmp_path):
    sender = EmailSenderViaFile(TEMPLATE, CUSTOMERS, tmp_path)
    sender.send_email()

    for output in EXPECTED_OUTPUT:
        recipient = output['to']
        expected_output_file = tmp_path / f'{recipient}.json'

        assert tmp_path.exists()
        assert expected_output_file.exists()

        email_obj = json.load(expected_output_file.open('r'))

        assert isinstance(email_obj, dict)
        assert email_obj == output
