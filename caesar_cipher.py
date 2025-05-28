def caesar(text,shift,encode_or_decode):
    new_text=""
    if encode_or_decode=="decode":
        shift*=-1
    for letter in text:
        if letter in alphabet:
            new_position=alphabet.index(letter)+shift
            if new_position>26:
                new_position%=26
            new_text+=alphabet[new_position]
        else:
            new_text+=letter
    print(f"The {encode_or_decode}d text is \"{new_text}\"")

should_continue=True
while should_continue:
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    restart=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart=="no":
        should_continue=False
        print("Goodbye")