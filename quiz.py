points = 0

# Första frågan
svar_1 = input('Är Niinistö Finlands president? ')

if svar_1.lower() == 'ja':
	points = points + 1
	
elif svar_1.lower == 'nej':
	points = points - 1

else:
	print("Svara 'ja' eller 'nej'!")

print("Du fick " + str(points) + " poäng!")