import unittest

import phone_formatter

# These should pass all tests:
VALID_PHONE_NUMBERS = [
    "+31 20 123 4567",
    "+31201234567",
    "+31(0)201234567",
    "+31 (0)20 123 4567",
    "+31 (0)20-123 4567",
    "020 123 4567",
    "020-123 4567",
    "(020) 123 4567",
    "(020)-123 4567",
]

# These may pass some tests but not the final one:
INVALID_PHONE_NUMBERS = [
    "(020)-123 456",
    "0031 123 4567",
    "0031-020 123 456",
    "020-123 4567 (ask for Mike)",
    "+32 1234567",
]  # too short, contains text, not Dutch


class TestSamplePhoneNumbers(unittest.TestCase):
    def test_determine_if_phone_number_is_valid(self):
        for phone_number in VALID_PHONE_NUMBERS:
            self.assertEqual(
                phone_formatter.phone_number_contains_only_valid_characters(
                    phone_number
                ),
                True,
            )

        some_invalid_character_phone_numbers = [
            "020-123 4567 (ask for Mike)",
            "020-123 4567/4568",
            "020_123_4567",
        ]

        for phone_number in some_invalid_character_phone_numbers:
            self.assertEqual(
                phone_formatter.phone_number_contains_only_valid_characters(
                    phone_number
                ),
                False,
            )

    def test_determine_if_phone_number_is_correct_length(self):
        for phone_number in VALID_PHONE_NUMBERS:
            self.assertEqual(
                phone_formatter.phone_number_is_9_or_10_digits_long(phone_number), True
            )

        some_invalid_character_phone_numbers = [
            "+32 123 4567",
            "+31201234523167",
            "020-123 4567/4568",
            "020_123_456",
            "+3220-123 4567",
        ]

        for phone_number in some_invalid_character_phone_numbers:
            self.assertEqual(
                phone_formatter.phone_number_is_9_or_10_digits_long(phone_number), False
            )

    def test_determine_if_phone_number_has_foreign_international_component(self):
        dutch_int_phone_numbers = ["+31 020 123 4567", "0031 20 123 4567"]
        foreign_int_phone_numbers = [
            "+32020 123 4567",
            "003220 123 4567",
            "+1 123 45678",
        ]
        non_int_phone_numbers = ["020 123 4567", "031 123 4567"]

        for phone_number in dutch_int_phone_numbers:
            self.assertEqual(
                phone_formatter.phone_number_is_foreign(phone_number),
                False,
            )

        for phone_number in foreign_int_phone_numbers:
            self.assertEqual(
                phone_formatter.phone_number_is_foreign(phone_number),
                True,
            )

        for phone_number in non_int_phone_numbers:
            self.assertEqual(
                phone_formatter.phone_number_is_foreign(phone_number),
                False,
            )

    def test_determine_if_phone_number_can_be_reformatted(self):
        for phone_number in VALID_PHONE_NUMBERS:
            self.assertEqual(
                phone_formatter.determine_if_phone_number_can_be_reformatted(
                    phone_number
                ),
                True,
            )

        for phone_number in INVALID_PHONE_NUMBERS:
            self.assertEqual(
                phone_formatter.determine_if_phone_number_can_be_reformatted(
                    phone_number
                ),
                False,
            )

    def test_reformatted_phone_number(self):
        for phone_number in VALID_PHONE_NUMBERS:
            self.assertEqual(phone_formatter.formatter(phone_number), "+31 20 123 4567")


if __name__ == "__main__":
    unittest.main()
