# import pandas as pd
import re
def is_name_in_csv(word,csv_file):
  with open(csv_file,"r") as f:
    data = f.read()
  return bool(re.search(word, data))

list_file_csv = ['content1.csv','content2.csv','content3.csv']
word = "18-03"
for csv_file in list_file_csv:
  if is_name_in_csv(word,csv_file):
    print(f"find the {word} in {csv_file}")