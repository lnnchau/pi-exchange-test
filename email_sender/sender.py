import json
import re

from pathlib import Path
from datetime import datetime


class EmailSender:
    def __init__(self, template, customers):
        self.template = template
        self.customers = customers
        self.email_objs = []

        self.__generate_email_objs()

    def __generate_email_objs(self):
        placeholders = re.findall(r'{{[A-Z\_]+}}', self.template['body'])
        email_objs = []

        for customer in self.customers:
            email_obj = self.template.copy()
            email_obj['to'] = customer['EMAIL']

            content = email_obj['body']
            for placeholder in placeholders:
                keyword = placeholder[2:-2]     # take out the curly brackets

                value = ''
                if keyword == 'TODAY':
                    value = datetime.now().strftime('%d %B %y')
                else:
                    value = customer[keyword]

                content = re.sub(placeholder, value, content)

            email_obj['body'] = content
            email_objs.append(email_obj)

        self._set_email_objs(email_objs)

    def set_template(self, template):
        self.template = template
        self.__generate_email_objs()

    def add_customer(self, customer_list):
        self.customers.extend(customer_list)
        self.__generate_email_objs()

    def _get_email_objs(self):
        return self.email_objs

    def _set_email_objs(self, email_objs):
        self.email_objs = email_objs

    def send_email(self):
        pass


class EmailSenderViaFile(EmailSender):
    def __init__(self, template, customers, output_dir):
        super().__init__(template, customers)

        if not Path(output_dir).exists():
            Path(output_dir).mkdir(parents=True)
        self.output_dir = output_dir

    def send_email(self):
        for email_obj in self._get_email_objs():
            recipient = email_obj['to']
            fn = Path(self.output_dir) / f'{recipient}.json'
            json.dump(email_obj, fn.open('w'), indent=2)
