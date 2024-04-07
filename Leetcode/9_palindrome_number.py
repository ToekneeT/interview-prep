#https://leetcode.com/problems/palindrome-number/description/

'''
# Turns into a string first.
def isPalindrome(x):
    x = str(x)
    # Apparently a single digit is a palindrome.
    if len(str(x)) == 1:
        return True
    # Can be equally split.
    if len(x) % 2 == 0:
        left = x[:len(x) // 2]
        right = x[len(x) // 2:]
    # The middle can be different, so if it's an odd length
    # then split and ignore the middle by adding 1 to the splicing.
    else:
        left = x[:len(x) // 2]
        right = x[len(x) // 2 + 1:]
    return left == right[::-1]
'''
'''
# Done without turning into a string
def isPalindrome(x):
    if x < 0:
        return False

    original = x
    reverse = 0
    while x != 0:
        # Grabs the ones digit.
        ones = x % 10
        # Multiplies reverse by 10 moving the ones digit over one.
        reverse = reverse * 10 + ones
        # Removes the ones digit
        x //= 10

    return reverse == original

# After thinking of this solution, I realized I could've just reversed the
# entire string on the first solution instead of splitting it in half
'''
# After our recursion lesson, I was thinking about some functions I could do for recursion.
# Realized I used a while loop for this, so thought it'd be possible to do.

# reverse should be 0 for a reverse.
# used to track the reversed number within the 
# recursion
def reverse_num(num: int, reverse: int) -> int:
    if num == 0:
        return reverse
    ones = num % 10
    return reverse_num(num // 10, reverse * 10 + ones)

def isPalindome(x):
    if x < 0:
        return False
    return x == reverse_num(x, 0)