# black_error_example_2.py

def multiply_numbers(a,b,c):
    return a*b*c  # Missing spaces around operator

def divide_numbers(a,b):
    return a/b  # Missing spaces around operator

def main():
    product = multiply_numbers(4,5,6)  # Missing spaces after commas
    quotient = divide_numbers(10,2)  # Missing spaces after commas
    print(f"Product: {product}, Quotient: {quotient}")

if __name__ == "__main__":
    main()
