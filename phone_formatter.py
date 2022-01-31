import re


def phone_number_contains_only_valid_characters(phone_number: str) -> bool:
    """Verify if the phone number contains any characters besides digits,
    whitespace, +, - or parenthesis"""
    find_invalid_characters = re.search("[^\d\s\+\-\(\)]", phone_number)
    if find_invalid_characters is not None:
        return False
    else:
        return True


def phone_number_is_9_or_10_digits_long(phone_number: str) -> bool:
    """Besides certain service numbers, Dutch phone numbers have 10 digits,
    including a leading zero, which may be omitted if international notation
    is used (ex. +31 20 123 4567, 0031 20 123 4567, 0031 (0)20 123 4567 and
    020 123 4567 are all valid)"""
    digits_only = "".join(re.findall("\d", phone_number))
    if digits_only.startswith("0031"):
        # check if there's a "0" right after the international number:
        if digits_only[4] == "0" and len(digits_only[4:]) == 10:
            return True
        elif digits_only[4] != "0" and len(digits_only[4:]) == 9:
            return True
        else:
            return False
    elif digits_only.startswith("31"):
        # check if there's a 0 right after the international number:
        if digits_only[2] == "0" and len(digits_only[2:]) == 10:
            return True
        elif digits_only[2] != "0" and len(digits_only[2:]) == 9:
            return True
        else:
            return False
    elif digits_only.startswith("0") and len(digits_only[1:]) == 9:
        return True
    else:
        return False


def phone_number_is_foreign(phone_number: str) -> bool:
    """Determines if the phone number starts with an international code '+'
    or '00' but is not +31 or 0031"""
    digits_and_plus_only = "".join(re.findall("\+?\d*", phone_number))
    if digits_and_plus_only.startswith("+"):
        if digits_and_plus_only[1:3] == "31":
            return False
        else:
            return True
    elif digits_and_plus_only.startswith("00"):
        if digits_and_plus_only[2:4] == "31":
            return False
        else:
            return True
    else:
        return False


def determine_if_phone_number_can_be_reformatted(phone_number: str) -> bool:
    if (
        not phone_number_is_foreign(phone_number)
        and phone_number_is_9_or_10_digits_long(phone_number)
        and phone_number_contains_only_valid_characters(phone_number)
    ):
        return True
    else:
        return False


def formatter(phone_number: str) -> str:
    if determine_if_phone_number_can_be_reformatted(phone_number):
        digits_and_plus_only = "".join(re.findall("\+?\d*", phone_number))
        # remove international component
        if digits_and_plus_only[0:3] == "+31":
            digits_and_plus_only = digits_and_plus_only[3:]
        elif digits_and_plus_only[0:4] == "0031":
            digits_and_plus_only = digits_and_plus_only[4:]
        else:
            digits_and_plus_only

        # remove leading zero:
        if digits_and_plus_only[0] == "0":
            digits_and_plus_only = digits_and_plus_only[1:]
        else:
            digits_and_plus_only
        return f"+31 {digits_and_plus_only[0:2]} {digits_and_plus_only[2:5]} {digits_and_plus_only[5:12]}"
    else:
        # leave unedited
        return phone_number
