def is_valid_parentheses(s: str) -> bool:
    """
    Return whether a string of (), {}, and [] brackets is balanced.

    Non-bracket characters are invalid. An empty string is balanced.
    """
    opening = {"(", "{", "["}
    matching = {")": "(", "}": "{", "]": "["}
    stack = []

    for character in s:
        if character in opening:
            stack.append(character)
        elif character in matching:
            if not stack or stack.pop() != matching[character]:
                return False
        else:
            return False

    return not stack
