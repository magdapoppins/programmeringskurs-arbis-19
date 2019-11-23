alphabet = ['a', 'b', 'c', 'd']

message = input("Mikä on viestisi?	").lower()
encrypted = ""

for letter in message:
	letter_index = alphabet.index(letter)

	new_letter_index = letter_index + 3

	if new_letter_index >= len(alphabet):
		new_letter_index = new_letter_index - len(alphabet)

	encrypted = encrypted + alphabet[new_letter_index]

print(encrypted)
