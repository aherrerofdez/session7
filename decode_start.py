alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"

try :
    fp = open("secret.txt")
    message = []
    message_decoded = []
    for line in fp :
        line_counter = 0
        for letter in line :
            if letter in vowel :
                line_counter += 1
        message.append(line_counter)
    fp.close()
    for index in message :
        letter_decoded = alphabet[index]
        message_decoded.append(letter_decoded)
    print(''.join(message_decoded))

except FileNotFoundError:
    print("The file was not found")