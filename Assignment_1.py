def shift_char(char, key, mode):
    # Check if the character is an alphabet letter
    if char.isalpha():
        # Determine the base ASCII value for lowercase or uppercase letters
        # ord is default function available in python for converting char to integer(ASCII)
        
        base = ord('a') if char.islower() else ord('A')
        if mode == 'encrypt':
            #calculating shifted value based on key and %26 ensure it wraps around alphabet range
            shifted = (ord(char) - base + key) % 26
        else:
            shifted = (ord(char) - base - key) % 26
        # chr function is used to convert interger to char
        return chr(base + shifted)
    else:
        return char

def process_message(message, key, mode):
    result = ''
    for char in message:
        # passing each character of message in shift_char function.
        result += shift_char(char, key, mode)
    return result

def main():
    # Take user input for the message, key, and mode
    message = input("Enter the message: ")
    key = int(input("Enter the key (an integer): "))
    mode = input("Choose mode (encrypt/decrypt): ").lower()

    # Check if the mode is valid 'encrypt' or 'decrypt'
    if mode != 'encrypt' and mode != 'decrypt':
        print("Invalid mode. Please choose encrypt or decrypt.")
        return

    result = process_message(message, key, mode)

    if mode == 'encrypt':
        print("Encrypted message:", result)
    else:
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
