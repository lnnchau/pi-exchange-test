from datetime import datetime


TEMPLATE = {
    "from": "The Marketing Team <marketing@example.com",
    "subject": "A new product is being launched soon...",
    "mimeType": "text/plain",
    "body": """
        Hi {{TITLE}} {{FIRST_NAME}} {{LAST_NAME}},\n
        Today, {{TODAY}}, we would like to tell you that... Sincerely,\nThe Marketing Team
        """
}

CUSTOMERS = [
    {
        "EMAIL": "john.smith@example.com",
        "TITLE": "Mr",
        "FIRST_NAME": "John",
        "LAST_NAME": "Smith"
    },
    {
        "EMAIL": "michelle.smith@example.com",
        "TITLE": "Mrs",
        "FIRST_NAME": "Michelle",
        "LAST_NAME": "Smith"
    }
]

TODAY = datetime.now().strftime('%d %B %y')

EXPECTED_OUTPUT = [
    {
        "from": "The Marketing Team <marketing@example.com",
        "subject": "A new product is being launched soon...",
        "mimeType": "text/plain",
        "body": f"""
            Hi Mr John Smith,\n
            Today, {TODAY}, we would like to tell you that... Sincerely,\nThe Marketing Team
            """,
        "to": "john.smith@example.com"
    },
    {
        "from": "The Marketing Team <marketing@example.com",
        "subject": "A new product is being launched soon...",
        "mimeType": "text/plain",
        "body": f"""
            Hi Mrs Michelle Smith,\n
            Today, {TODAY}, we would like to tell you that... Sincerely,\nThe Marketing Team
            """,
        "to": "michelle.smith@example.com"
    }
]