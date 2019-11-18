import os
import datetime

diary_path = "C:/Users/magda/Desktop/diary.txt"

if not os.path.exists(diary_path):
    print("Check the location of your diary!: ", diary_path)
    with open(diary_path, "a") as new_diary_file:
        new_diary_file.write("DIARY 🌈")


with open(diary_path, "a") as diary:
    date = datetime.datetime.now()
    date_string = f"{date.day}/{date.month}/{date.year}"
    memo_topic = input("Topic:\t")
    memo_text = input("Text:\t")
    diary.writelines(
        f"Date:\t{date_string} {os.linesep}Topic:\t{memo_topic} {os.linesep}")
    diary.writelines(memo_text)
    diary.writelines(f"{os.linesep}---{os.linesep}")
