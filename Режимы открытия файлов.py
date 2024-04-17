from pprint import pprint

faile_name = "Alex.txt"
faile = open(faile_name, mode="r", encoding="utf-8")
file_content = faile.read()
faile.close()
pprint(file_content.split("\n"))

