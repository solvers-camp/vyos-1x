import os, sys # Multiple imports on one line

def unused_function():
    pass  # This function is defined but never used

def greet(name):
    print(f"Hello, {name}")

def main():
    greet("World")

if __name__ == "__main__":
    main()
