import random

def generate_password(length):
    # Define possible characters for the password
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_characters = '!@#$%^&*()'

    # Combine all possible characters into one string
    all_characters = lowercase + uppercase + digits + special_characters
    
    password = ""
    for i in range(length):
        password += random.choice(all_characters)
    
    return password

def main():
    # Ask the user for the desired password length
    length = int(input("Enter the desired password length: "))
    
    # Generate and display the password
    passsword = generate_password(length)
    print("Generated Password:", passsword)

if __name__ == "__main__":
    main()
