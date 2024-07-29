def mirror_string(s):
    """
    This function takes a string s and returns its mirror image.
    """
    return s[::-1]

# Example usage
if __name__ == "__main__":
    input_string = "hello"
    print(f"Original: {input_string}")
    print(f"Mirrored: {mirror_string(input_string)}"  # Missing closing parenthesis

def unused_function():
    pass  # This function is defined but never used, which should be flagged by ruff
