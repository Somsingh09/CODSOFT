import random
import string

def generate_password(length=12):
    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure password has at least one of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length
    password += random.choices(characters, k=length-4)
    
    # Shuffle the password list to randomize order
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(12))
