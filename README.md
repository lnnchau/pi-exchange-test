# Pi Exchange - Software Engineer - Case Study

## Quick start
- Clone the Docker image `docker pull lnnchau/pi-exhange:v1.0.0`
- Run the command below. The output should be stored in `/path/to/output_emails` and `/path/to/error/folder` (if any)
    ```
    docker run --rm -v /path/to/template.json:/data/input/template.json -v /path/to/customers.csv:/data/input/customers.csv -v /path/to/output_emails:/data/output -v /path/to/error/folder:/data/errors lnnchau/pi-exhange:v1.0.0
    ```
    Please be noted that since `errors.csv` is not created initially and we're mounting volumes into docker containers, `/path/to/error/folder` would be used in place of `/path/to/error/folder/errors.csv` as in the requirements.

## Run in Docker container
- To directly run the application in its environment, run
    ```
    docker run --rm -v /path/to/template.json:/data/input/template.json -v /path/to/customers.csv:/data/input/customers.csv -v /path/to/output_emails:/data/output -v /path/to/error/folder:/data/errors -it lnnchau/pi-exhange:v1.0.0 /bin/bash
    ```
- Run tests. All tests should be passed
    ```
    python3 -m pytest
    ```
- Run the command:
    ```
    python3 cli.py /path/to/email_template.json /path/to/customers.csv /path/to/output_emails/ /path/to/errors.csv
    ```

## Contributing
### Add new sending methods
New sending methods can be implemented by inheriting class `EmailSender` in `email_sender/sender.py`. For example:
```python
class EmailSenderViaSMTP(EmailSender):
    def __init__(self, template, customers):
        super().__init__(template, customers)

        # some new logic (if any)

    def send_email(self):
        for email_obj in self._get_email_objs():
            send_smtp(email_obj)

            # do something here
```
Please check out the source code for more information

### Update .csv file format
If you want to update format of customers csv file, update `columns` in function `json_to_csv` in `email_sender/utils.py`. For example:
```python
def json_to_csv(obj, fp):
    """
    Convert JSON back to CSV file with original format
    """
    columns = ['TITLE', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'NEW_COL_1', 'NEW_COL_2']
    return pd.DataFrame.from_dict(obj)[columns].to_csv(fp, index=False)
```