import secrets
import string

def create_mixed_password():
    print("--- Secure Password Generator ---")

    try:

        length = int(input("How many characters long should the password be? "))

        if length < 8:
            print("Note: Your password should be .")

        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation

        all_chars = letters + numbers + symbols

        password = "".join(secrets.choice(all_chars) for _ in range(length))

        print(f"\nYour new strong password: {password}")

    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    create_mixed_password()
