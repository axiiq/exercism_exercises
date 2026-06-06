def is_paired(input_string):
    stack = []
    matching_brackets = {")": "(", "}": "{", "]": "["}
    
    for char in input_string:
        if char in matching_brackets.values():
            stack.append(char)
            
        elif char in matching_brackets.keys():
            if not stack or stack.pop() != matching_brackets[char]:
                return False

    return len(stack) == 0