def check_type(obj):
    if isinstance(obj, str):
        print(f"{obj} is a string.")
    elif isinstance(obj, int):
        print(f"{obj} is an integer.")
    else:
        print(f"{obj} is neither a string nor an integer.")

# Test with different types
check_type("Hello")  # Output: Hello is a string.
check_type(42)       # Output: 42 is an integer.
check_type(3.14)     # Output: 3.14 is neither a string nor an integer.
