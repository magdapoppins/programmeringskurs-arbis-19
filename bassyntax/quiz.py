def check_answer(guess, answer):
	global points

	if guess.lower() == answer.lower():
		points += 1
		print("Rätt!")
	else:
		print("Inte riktigt...")

points = 0
print("Dags för quiz!")
print("--------------")

guess1 = input('Är Niinistö Finlands president?			')
check_answer(guess1, 'ja')
guess1 = input('Vilken var Finlands första huvudstad?		')
check_answer(guess1, 'Åbo')
guess1 = input('I vilken stad ligger museet Kiasma?		')
check_answer(guess1, 'Helsingfors')

print("---------------")
print("Du fick " + str(points) + " poäng!")