def get_valid_input(prompt="Answer: "):
    """
    Continuously prompts the user until they enter a number between 15 and 114 (inclusive).
    Returns the validated integer input.
    """
    while True:
        try:
            value = int(input(prompt))
            if 14 < value < 115:
                return value
        except ValueError:
            pass  # Ignore invalid input and prompt again

def calculate_boys_and_girls(boys_and_girls):
    """
    Given the validated input, calculate the number of boys and girls.
    Returns a tuple (boys, girls).
    """
    answer = boys_and_girls - 15
    girls = answer % 10
    boys = (answer - girls) // 10
    return boys, girls

def print_result(boys, girls):
    """
    Prints the result in a grammatically correct format.
    """
    if boys == 1 and girls != 1:
        print(f"You have 1 boy and {girls} girls")
    elif girls == 1 and boys != 1:
        print(f"You have {boys} boys and 1 girl")
    elif girls == 1 and boys == 1:
        print("You have 1 boy and 1 girl")
    else:
        print(f"You have {boys} boys and {girls} girls")

def main():
    boys_and_girls = get_valid_input()
    boys, girls = calculate_boys_and_girls(boys_and_girls)
    print_result(boys, girls)

if __name__ == "__main__":
    main()
