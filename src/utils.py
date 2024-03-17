import json


def get_data(is_main: bool = False) -> list:
    """Read data from json file where 'state==EXECUTED'"""
    if is_main:
        path = "./data/operations.json"
    else:
        path = "../data/operations.json"

    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        return [operation for operation in data if operation.get("state", "") == "EXECUTED"]


def get_last_operations(data: list, size: int) -> list:
    """Return last N operations from sorted data"""
    return sorted(data, key=lambda operation: operation.get("date"), reverse=True)[:size]


def format_date(date: str) -> str:
    """Format date in russian format"""
    date_parts = date.split("T")[0].split("-")[::-1]
    return ".".join(date_parts)


def format_account(text: str) -> str:
    """Get account in russian format"""
    account_parts = text.split()

    account_number = account_parts.pop()
    account_name = " ".join(account_parts)

    if account_name.lower() == "счет" or account_name.lower() == "счёт":
        account_number = f"**{account_number[-4:]}"
    else:
        account_number = f"{account_number[:4]} {account_number[4:6]}** **** {account_number[-4:]}"

    return f"{account_name} {account_number}"


def format_operation(operation: dict) -> str:
    """Get operation in recommended format"""
    lines = [f"{format_date(operation['date'])} {operation['description']}"]

    if "from" in operation:
        lines.append(f"{format_account(operation['from'])} -> {format_account(operation['to'])}")
    else:
        lines.append(f"{format_account(operation['to'])}")

    amount_data = operation['operationAmount']

    lines.append(f"{amount_data['amount']} {amount_data['currency']['name']}")

    return "\n".join(lines)


def format_operations(data: list) -> str:
    """Get all operations in recommended format"""
    lines = []

    for operation in data:
        lines.append(format_operation(operation))

    return "\n\n".join(lines)
