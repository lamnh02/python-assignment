list_file_csv = ['content1.csv', 'content2.csv', 'content3.csv']
 
def search(key_word: str, list_file_csv: list):
    print("Từ khóa: " + key_word +"\n")
 
    prior_dict = dict()
    for i in list_file_csv:
        prior_dict[i] = 0.0
 
    key_word = key_word.lower()
    key_separate = key_word.split()
 
    for csv_file in list_file_csv:
        with open(csv_file, "r", encoding="utf8") as f:
            data = f.read()
            data = data.lower()
            x = data.count(key_word)
            if x >= 1:
                prior_dict[csv_file] += (100 + (x-1)*10)
            for key in key_separate:
                y = data.count(key)
                if y > x and x == 0:
                    prior_dict[csv_file] += (1 + (y-x-1)*0.5)
                elif y > x and x != 0:
                    prior_dict[csv_file] += ((y-x)*0.5)
 
    prior_dict = dict(sorted(prior_dict.items(), key=lambda item: item[1], reverse = True))
 
    print("Kết quả search theo độ ưu tiên:\n")
 
    for key in prior_dict:
        if prior_dict[key] > 0:
            print(key + "\n")
    print("------------------------")
 
 
while(True):
    key_word = input("enter input: ")
    search(key_word, list_file_csv)