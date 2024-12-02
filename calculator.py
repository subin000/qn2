def calculate_square(number):
    # Incorrect logic: returns cube instead of square
    return number ** 3

if __name__ == "__main__":
    print(calculate_square(2))  # Expected: 4, Bug: Returns 8
