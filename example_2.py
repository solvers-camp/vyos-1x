# black_error_example.py

def add_numbers(a,b,c):
    return a+b+c  # Missing spaces around operators

def main():
    result = add_numbers(1,2,3)  # Missing spaces after commas
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
