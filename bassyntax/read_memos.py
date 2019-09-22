import os

memo_file_path = "/Users/magdapoppins/Desktop/programmeringskurs-arbis-19/bassyntax/memos.txt"
contents = []

if os.path.exists(memo_file_path):
    print("Memo file exists.")
    memo = open(memo_file_path)
    for line in memo:
        contents.append(line)
    memo.close()

print("MEMOS:")
print("-------------")
for line in contents:
    print(line)
print("-------------")

