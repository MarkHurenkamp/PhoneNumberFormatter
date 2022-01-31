import pandas as pd

import phone_formatter

valid_data = {
    "valid 1": {
        "comment": "expected outcome",
        "phone number": "+31 20 123 4567",
    },
    "valid 2": {"comment": "int, no spaces", "phone number": "+31201234567"},
    "valid 3": {"comment": "int + zero", "phone number": "+31(0)201234567"},
    "valid 4": {"comment": "int + zero + spaces", "phone number": "+31 (0)20 123 4567"},
    "valid 5": {"comment": "as above + dash", "phone number": "+31 (0)20-123 4567"},
    "valid 6": {"comment": "no int, has spaces", "phone number": "020 123 4567"},
    "valid 7": {"comment": "as above + dash", "phone number": "020-123 4567"},
    "valid 8": {
        "comment": "no int, parentheses and space",
        "phone number": "(020) 123 4567",
    },
    "valid 9": {"comment": "as above + dash", "phone number": "(020)-123 4567"},
    "valid 10": {"comment": "no int mobile number", "phone number": "06 12345678"},
    "valid 11": {"comment": "int mobile number", "phone number": "+31 (0)6 12345678"},
    "valid 12": {
        "comment": "int mobile number + dashes",
        "phone number": "+31 6 1234-5-678",
    },
}

invalid_data = {
    "invalid 1": {"comment": "too short", "phone number": "(020)-123 456"},
    "invalid 2": {
        "comment": "int 0031, but too short",
        "phone number": "0031 123 4567",
    },
    "invalid 3": {"comment": "int +31, but too short", "phone number": "+31 123 4567"},
    "invalid 4": {
        "comment": "int 0031, but too short with zero",
        "phone number": "0031 020 123 456",
    },
    "invalid 5": {
        "comment": "int +31, but too short with zero",
        "phone number": "+31 020 123 456",
    },
    "invalid 6": {
        "comment": "phone number with text",
        "phone number": "020-123 4567 (ask for Mike)",
    },
    "invalid 7": {
        "comment": "international, foreign country",
        "phone number": "+32 123 4567",
    },
    "invalid 8": {
        "comment": "international, foreign country",
        "phone number": "+32 123 4567",
    },
}

known_exceptions = {
    "known exception 1": {"comment": "emergency number", "phone number": "112"},
    "known exception 2": {
        "comment": "city hall service number",
        "phone number": "14 038",
    },
    "known exception 3": {
        "comment": "police, non-emergency",
        "phone number": "0900-8844",
    },
}

valid_df = pd.DataFrame.from_dict(valid_data, orient="index")
invalid_df = pd.DataFrame.from_dict(invalid_data, orient="index")
known_exceptions_df = pd.DataFrame.from_dict(known_exceptions, orient="index")
combined_df = pd.concat([valid_df, invalid_df, known_exceptions_df])

combined_df["output"] = combined_df["phone number"].apply(
    lambda x: phone_formatter.formatter(x)
)

print(combined_df)
