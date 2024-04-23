# https://leetcode.com/problems/valid-parentheses/

# A stack is important as we want the order of the parenthesis
# to close in the correct order.
# e.x. (){} closes nicely.
# Stack -> (, {
# Stack push (, sees closed paren, converts to open equivalent,
# pops stack => (, does ( == (, yes, move on.
# e.x. ({)} doesn't close nicely.
# Stack push (, stack push {, sees a closed paren, converts to open equivalent,
# pops stack => {, does { == (, no, return False.
def isValid(s: str) -> bool:
    # Dictionary where the closed parenthesis is matched to the open.
    # Will be used when receiving a closed parenthesis, we then grab the value
    # which would be an open parenthesis and compare it to an element in the stack
    # that only contains open parenthesis.
    paren_key = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    # Stack will contain only open parenthesis.
    stack_open = []
    # c is the character of the string.
    for c in s:
        # Checks if the character is an open parenthesis. If it is, it'll push
        # the element into the stack.
        if c in paren_key.values():
            stack_open.append(c)
        # If the element isn't an open parenthesis, then it's a closed.
        else:
            # First checks if the stack is empty, if it is, then we received a closed parenthesis
            # before an open, so it instantly fails.
            if len(stack_open) == 0:
                return False

            # If there is an element in the stack, then we compare it to the current item in the string.
            # In this case, it's a closed parenthesis, which we'll stick into the dictionary key; giving us a
            # open parenthesis equivalent. If the open parenthesis equivalent is the same as the one in the stack,
            # we move on and check the rest, otherwise we return False.
            value = stack_open.pop()
            if paren_key[c] != value:
                return False
    # If there are elements in the stack, then something wasn't closed properly.
    return len(stack_open) == 0