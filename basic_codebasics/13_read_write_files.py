"""
https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/read_write_file_exercise.md
question link
"""

# exercise 1

dict = { }
with open("C:\\Users\\Khin Thandar Kyaw\\Documents\\Python\\basic_codebasics\\poem.txt", "r")as f:
    for line in f:
        tokens = line.split(" ")
        for token in tokens:
            if token in dict:
                dict[token] += 1
            else:
                dict[token] = 1

print(dict)

num = list(dict.values())
max_num = max(num)

print("Words with maximum occurences are : ")
for key, val in dict.items():
    if max_num == val:
        print(key)

# exercise 2

with open("C:\\Users\\Khin Thandar Kyaw\\Documents\\Python\\basic_codebasics\\stocks.csv", "r")as f, open("C:\\Users\\Khin Thandar Kyaw\\Documents\\Python\\basic_codebasics\\output.csv", "w")as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    next(f)  # This will skip first line in the file which is a header
    for line in f:
        tokens = line.split(",")
        cp_name = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book_val = float(tokens[3])
        pe_rt = round(price/eps, 2)
        pb_rt = round(price/book_val, 2)
        out.write(f"{cp_name},{pe_rt},{pb_rt}\n")

with open("C:\\Users\\Khin Thandar Kyaw\\Documents\\Python\\basic_codebasics\\output.csv", "r") as f:
    for line in f:
        tokens = line.split(" ")
        print(tokens)