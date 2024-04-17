faile_name = "Alex.txt"
with open(faile_name, mode="r", encoding="utf-8") as file:
    for line in file:
        print(line, end='')
