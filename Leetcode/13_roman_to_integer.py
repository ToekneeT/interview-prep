# In this solution, I originally had a for loop instead of a 
# while loop. I kept the i += 1 in the nested conditionals,
# but realized that when the for loop would iterate, it'd just
# overwrite the i anyway.
# Spent a few minutes trying to figure out what to do with that,
# before realizing I could just swap it with a while loop.
# Overall, this problem wasn't hard, maybe spent 30 minutes on it total.
# Didn't have to look up any extra information.
# I'm not too happy with the nested conditionals.

# Time complexity: O(n), goes through the string once worst case.
def romanToInt(s: str) -> int:
    roman_to_int = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }
    # There are a few cases with roman numerals where it'll take
    # the previous roman numeral and the current one and give it a
    # different value.
    # For example, IV = 4, instead of a 1 and a 5.
    # XC = 90 instead of 10 and 100.
    # By having the special cases set, it can be used later to check
    # if the current letter is a special case or not.
    special_case = ["I", "X", "C"]
    two_letter_roman = ""
    number = 0
    i = 0
    while i < len(s):
        if i + 1 != len(s):
            if s[i] in special_case:
                two_letter_roman = s[i] + s[i + 1]
                if two_letter_roman in roman_to_int:
                    number += roman_to_int[two_letter_roman]
                    i += 1
                else:
                    number += roman_to_int[s[i]]
            else:
                number += roman_to_int[s[i]]
        else:
            number += roman_to_int[s[i]]
        i += 1
    return number