alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(original_text,shift_amount,enocde_decode):
    output_text=""
    if enocde_decode=="decode":
                shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            shifted_position=alphabet.index(letter)+shift_amount
            shifted_position%=len(alphabet)
            output_text+=alphabet[shifted_position]

    print(f"your {enocde_decode}d text is {output_text}")
should_condition=True

while should_condition:


    direction=input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    
    ceaser(original_text=text,shift_amount=shift,enocde_decode=direction)
    restart=input("you want to continue decoding \n").lower()
    if restart=='no':
        should_condition=False
        print("Goodbye")

