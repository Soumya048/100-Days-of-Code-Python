from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    output_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amount
                if (new_position > 25):
                    new_position = new_position % 26
                    output_text += alphabet[new_position]
                else:
                    output_text += alphabet[new_position]
            elif cipher_direction == "decode":
                new_position = position - shift_amount
                if (new_position < 0):
                    new_position = new_position + 26
                    output_text += alphabet[new_position]
                else:
                    output_text += alphabet[new_position]
            else:
                print("Enter a valid choice")
        else:
            output_text += char
    print(f"The {cipher_direction}d text is {output_text}")


input_choice = "yes"

while input_choice == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    input_text = input("Type your message:\n").lower()
    input_shift = int(input("Type the shift number:\n"))
    caesar(start_text=input_text,
           shift_amount=input_shift,
           cipher_direction=direction)
    print("-------------------------------")
    input_choice = input("Type 'yes' if you want to do again?:\n").lower()

print("-------------------------------")
print("Goodbye")
