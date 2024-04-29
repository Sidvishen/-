class InvalidDataException(Exception):
    pass
class ProcessingException(Exception):
    pass
def process_data(data):
    if not isinstance(data, int):
        raise InvalidDataException("Неверный тип данных")
    if data < 0:
        raise ProcessingException("Отрицательные данные не допускаются")
    return data * 2
def main_function(input_data):
    try:
        result = process_data(input_data)
        print("Результат после обработки:", result)
    except InvalidDataException as e:
        print('Ошибка неверных данных:', e)
        raise
    except ProcessingException as e:
        print('Ошибка обработки:', e)
        raise

if __name__ == '__main__':
    try:
        main_function(10)
        main_function(-5)
        main_function("abc")
    except Exception as e:
        print("Исключение поймано:")