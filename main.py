from src import utils


def print_lines():
    data = utils.get_data(True)
    data = utils.get_last_operations(data, 5)

    lines = []

    for operation in data:
        lines.append(utils.format_operation(operation))

    print("\n\n".join(lines))


if __name__ == '__main__':
    print_lines()
