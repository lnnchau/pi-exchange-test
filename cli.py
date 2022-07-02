import click
import json
from email_sender.utils import csv_to_json
from email_sender.sender import EmailSenderViaFile


@click.command()
@click.argument('template_fp', type=click.Path(exists=True))
@click.argument('customers_fp', type=click.Path(exists=True))
@click.argument('output_dir', type=click.Path())
@click.argument('error_fp', type=click.Path())
def send_mail(template_fp, customers_fp, output_dir, error_fp):
    customers = csv_to_json(customers_fp)
    template = json.load(open(template_fp))

    sender = EmailSenderViaFile(template, customers, output_dir, error_fp)
    sender.send_email()


if __name__ == '__main__':
    send_mail()
