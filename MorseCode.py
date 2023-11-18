MORSE_CODE = {'A': '.-', 'B': '-...',

                  'C': '-.-.', 'D': '-..', 'E': '.',

                  'F': '..-.', 'G': '--.', 'H': '....',

                  'I': '..', 'J': '.---', 'K': '-.-',

                  'L': '.-..', 'M': '--', 'N': '-.',

                  'O': '---', 'P': '.--.', 'Q': '--.-',

                  'R': '.-.', 'S': '...', 'T': '-',

                  'U': '..-', 'V': '...-', 'W': '.--',

                  'X': '-..-', 'Y': '-.--', 'Z': '--..',

                  '1': '.----', '2': '..---', '3': '...--',

                  '4': '....-', '5': '.....', '6': '-....',

                  '7': '--...', '8': '---..', '9': '----.',

                  '0': '-----', ' ': '/'}

converded_word = input("What do you want me to translate into the Morse code? ").upper()

code = ''
for letter in converded_word:
    code += MORSE_CODE[letter]

print(f'Word {converded_word} in Morse code is {code}')
