from __future__ import unicode_literals


from us_area_code.data import area_codes


class AreaCodeError(Exception):
    pass


def get_state_from_area_code(area_code):
    for state, codes in area_codes.items():
        if area_code in codes:
            return state
    return None


def get_area_codes_from_state(state):
    return area_codes.get(state, None)


def clean_number(number):
    _numbers = []
    for n in str(number):
        try:
            _numbers.append(str(int(n)))
        except ValueError:
            pass
    return "".join(_numbers)


def get_area_code_from_phone_number(phone_number):
    phone_number = clean_number(phone_number)
    if 11 < len(phone_number) < 10:
        raise AreaCodeError("Invalid Phone Number")
    if len(phone_number) == 10:
        return phone_number[:3]
    return phone_number[1:4]


def get_state_from_phone_number(phone_number):
    try:
        return get_state_from_area_code(get_area_code_from_phone_number(phone_number))
    except AreaCodeError:
        return None
