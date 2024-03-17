
def calc_units(value: int, unit_0: str, unit_1: str, unit_2: str) -> str:
    reminder = value % 100

    if 11 <= reminder <= 19:
        return unit_0

    reminder = reminder % 10

    if reminder == 1:
        return unit_1
    elif 2 <= reminder <= 4:
        return unit_2
    else:
        return unit_0
