import random
import string

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security.")
    
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure the password contains at least one character from each set
    all_characters = lowercase + uppercase + digits + special
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

# Generate a random strong password of 12 characters
print(generate_password(12))