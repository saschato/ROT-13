import string
import sys

def shift(key,char):
    chars = string.ascii_uppercase
    if char == " ":
        return char
    else:
        index = chars.find(char)
        return chars[(index+key)%26]

def main(text):
    new_string,counter = "",1
    for key in [13,13]:
        try:
            for char in text:
                new_string += shift(key,char)
        except KeyboardInterrupt:
            sys.exit()

        print(f" [+] pass {counter}:\t" + new_string)
        text = new_string
        new_string = ""
        counter += 1

if __name__ == "__main__":
    plain = input(" [+] enter plaintext: ").upper()
    print(f" [+] plaintext:\t{plain}")

    main(plain)
