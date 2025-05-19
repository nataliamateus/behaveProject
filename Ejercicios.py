from typing import Any


class IntegerToRoman:

    def __init__(self) -> None:
        # Define the Roman numeral symbols and their corresponding integer values
        self.roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def int_to_roman(self, num):
        """
        Convert an integer to a Roman numeral.

        :param num: Integer to be converted to a Roman numeral.
        :return: A string representing the Roman numeral.
        """
        if not 1 <= num <= 3999:
            raise ValueError("Number out of range (must be 1..3999)")

        roman_string = ""

        # Iterate through the Roman numeral symbols
        for value, symbol in self.roman_numerals:
            while num >= value:
                roman_string += symbol
                num -= value

        return roman_string


# Example usage
converter = IntegerToRoman()
print(converter.int_to_roman(25))  # Output: MCMLXXXVII
