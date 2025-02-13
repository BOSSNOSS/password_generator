import random

# Define lists of characters to use in password generation
LETTERS = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SYMBOLS = ["!", "#", "$", "%", "&", "@", "(", ")", "*", "+"]

def get_user_preferences():
    """
    Get user input for the number of letters, numbers, and symbols in the password.
    
    Returns:
        tuple: Number of letters, numbers, and symbols requested by the user.
    """
    print("Welcome to myPassword Generator App.\n")
    n_letters = int(input("How many letters would you like in your password:\n"))
    n_numbers = int(input("How many numbers would you like in your password:\n"))
    n_symbols = int(input("How many symbols would you like in your password:\n"))
    return n_letters, n_numbers, n_symbols

def generate_password(n_letters, n_numbers, n_symbols):
    """
    Generate a random password based on the specified number of letters, numbers, and symbols.
    
    Args:
        n_letters (int): Number of letters in the password.
        n_numbers (int): Number of numbers in the password.
        n_symbols (int): Number of symbols in the password.
    
    Returns:
        str: Generated password.
    """
    password_list = []
    
    # Add random letters to the password list
    for _ in range(n_letters):  # Using _ here because we don’t need the loop variable
        password_list.append(random.choice(LETTERS))
    
    # Add random numbers to the password list
    for _ in range(n_numbers):  # Using _ here because we don’t need the loop variable
        password_list.append(random.choice(NUMBERS))
    
    # Add random symbols to the password list
    for _ in range(n_symbols):  # Using _ here because we don’t need the loop variable
        password_list.append(random.choice(SYMBOLS))
    
    # Shuffle the list to randomize character order
    random.shuffle(password_list)
    
    # Convert list to string
    return ''.join(password_list)
