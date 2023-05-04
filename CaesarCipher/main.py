

# def caesar(text, shift, direction):
#     if direction == "encode":
#         cypherText = ""
#         for letter in text:
#             position = alphabet.index(letter)
#             newPosition = position + shift
#             cypherLetter = alphabet[newPosition]
#             cypherText += cypherLetter
#         print(f"The encoded text is {cypherText}")
#     elif direction == "decode":
#         cypherText = ""
#         for letter in text:
#             position = alphabet.index(letter)
#             newPosition = position - shift
#             cypherLetter = alphabet[newPosition]
#             cypherText += cypherLetter
#         print(f"The encoded text is {cypherText}")
#     else:
#         print("Please chose encode or decode")
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


def caesar(text, shift, direction):
    cypherText = ""
    shift = shift % 26
    if direction == "decode":
        shift = shift * -1
    for letter in text:
        if letter not in alphabet:
            cypherText += letter
        else:
            position = alphabet.index(letter)
            newPosition = position + shift
            newLetter = alphabet[newPosition]
            cypherText += newLetter
    print(f"The {direction} text is {cypherText}")


is_continue = True
while is_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    check = input("Type 'yes' if you want to go again. Otherwise type 'no' \n")
    if check == "no":
        is_continue = False
print("Goodbye")
