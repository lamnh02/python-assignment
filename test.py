# import pandas as pd
import re


def is_name_in_csv(word, csv_file):
    with open(csv_file, "r", encoding="utf8") as f:
        data = f.read()
    return bool(re.search(word, data))


list_file_csv = ['content1.csv', 'content2.csv', 'content3.csv']
word = "email"
for csv_file in list_file_csv:
    if is_name_in_csv(word, csv_file):
        print(f"""find "{word}" in {csv_file}""")
        print("\n")
        with open(csv_file, "r", encoding="utf8") as f:
            print(f.read())