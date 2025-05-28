Caesar Cipher Encoder/Decoder
A simple Python script that encrypts and decrypts messages using the classic Caesar Cipher technique.

🔍 Overview
The Caesar Cipher is a basic encryption method where each letter in the plaintext is shifted a certain number of places down or up the alphabet. This script allows users to:
.Encrypt messages by shifting letters forward.
.Decrypt messages by shifting letters backward.
.Preserve non-alphabetic characters (e.g., numbers, punctuation).
.Interact through a user-friendly command-line interface.

🚀 Getting Started
Prerequisites
.Python 3.x installed on your system.

Installation
1)Clone the repository:
  git clone https://github.com/harshvardhan60792/caesar_cipher.git
2)Navigate to the project directory
  cd caesar-cipher
3)Run the script:
  python caesar_cipher.py


🛠 Usage
Upon running the script, follow the prompts:
Choose the operation: type 'encode' to encrypt or 'decode' to decrypt.
Enter your message.
Specify the shift number (an integer).
View the result.
Decide whether to perform another operation or exit.

Example
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
3
The encoded text is "khoor zruog"
Type 'yes' if you want to go again. Otherwise type 'no'.
no
Goodbye

📄 Code Overview
The script defines a caesar function that handles both encoding and decoding based on user input. It shifts each alphabetic character by the specified amount, wrapping around the alphabet as necessary. Non-alphabetic characters are left unchanged.

🧪 Testing
To test the script:
1)Run the script using Python.
2)Follow the on-screen prompts to input messages and shift values.
3)Verify that the output matches expected results.

📌 Notes
The script converts all input text to lowercase to maintain consistency.
The alphabet list is redefined in each iteration; for optimization, consider defining it once outside the loop.

📄 License
This project is open-source and available under the MIT License.
