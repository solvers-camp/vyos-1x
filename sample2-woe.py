def greet(name: str) -> str:
    """
    Generate a greeting message.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def main() -> None:
    """
    Main function to execute the greeting.
    """
    name = "Butterfly"
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
