# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?

restart = True
while restart:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction != 'encode' and direction != 'decode':
            print("Please enter either 'encode' or 'decode':")
        else:
            break


    is_valid_input = False

    while not is_valid_input:
        text = input("Type your message:\n").lower()
        for letter in text:
            if letter not in alphabet:
                print("Please enter a valid text.\n")
                is_valid_input = False
                break
            else:
                is_valid_input = True


    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart_query = input("Do you wish to continue? Y or N\n").lower()

    if restart_query == "n":
        restart = False
        print("See you next time!")



