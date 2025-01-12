text = input("Введите текст на русском или английском")
shift = int(input("Введите значение сдвига "))

encrypted_text = ""

for letter in text:
    if letter == " ":
        encrypted_text += letter
        continue

    letter_index = ord(letter)
    letter_index += shift
    letter_out = chr(letter_index)
    encrypted_text += letter_out

print(encrypted_text)