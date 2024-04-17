from pprint import pprint

faile_name = "Alex.txt"
faile = open(faile_name, mode="rb")
file_content = faile.read()
faile.close()
pprint(file_content)


