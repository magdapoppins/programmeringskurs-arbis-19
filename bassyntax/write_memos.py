import os

memo_file_path = "/Users/magdapoppins/Desktop/programmeringskurs-arbis-19/bassyntax/memos.txt"

if os.path.exists(memo_file_path):
    print("Memo file exists.")
    memo = open(memo_file_path, 'r+')
    
    new_memo = input("Lägg till ny memo:    ")

    for line in memo:
        print(line)
    print(new_memo)

    memo.write("\n" + new_memo)

    memo.close()