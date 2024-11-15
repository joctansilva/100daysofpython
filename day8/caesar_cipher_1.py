import caesar_logo
print(caesar_logo.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amout, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amout *= -1
    
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:        
            shifted_position = alphabet.index(letter) + shift_amout
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
    
    direction = input("\nType 'encode' to encrypt, or 'decode' to decrypt:\n\n").lower()
    text = input("\nType your message:\n\n").lower()
    shift = int(input("\nType the shift amout:\n\n")) 
    
    caesar(original_text=text, shift_amout=shift, encode_or_decode=direction)

    restart = input("\nType 'yes' if you wat to go again. Otherwise type 'no':\n\n").lower()
    if restart == "no":
        should_continue = False
        print("\nGoodbye!")