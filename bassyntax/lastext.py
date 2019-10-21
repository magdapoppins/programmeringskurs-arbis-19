import os

path_to_memos = "C:/programmeringskurs/bassyntax/memos.txt"

print(os.path.exists(path_to_memos))

if os.path.exists(path_to_memos):
	print("Memo.txt exists.")
	ny_memo = input("Skriv ny memo:	")

	memo = open(path_to_memos, 'r+')

	for line in memo:
		print(line)

	memo.write("\n" +ny_memo)
	memo.close()