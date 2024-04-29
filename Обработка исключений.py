def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def read_file(filename):
    try:
        with open(filename, 'r') as file: return file.read()
    except FileNotFoundError:
        return None
    except UnicodeDecodeError:
        return None

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except ValueError:
        return None

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None
    except TypeError:
        return None
  