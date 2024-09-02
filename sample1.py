def example_function():
    print("This line exceeds the 30 character limit and should be flagged by the linter testing ruff.toml")
    print("This line exceeds does not exceed 30 character")
    if True:
        print("This line is indented with 4 spaces")# Spacing Error
    else:
        print("This line is also indented with 4 spaces.")
