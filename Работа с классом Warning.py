import warnings

def function_with_warnings():
    try:
        print('Предупреждение')
        warnings.warn('Внимание', UserWarning)
    except UserWarning as e:
        print({e})
def safe_division(a, b):
    if (a) < 0.01:
        print(a, 'Меньше нуля')
    return a / b

a = 10
b = 0.001
result = safe_division(a, b)
print(f'Результат деления: {result}')

warnings.simplefilter('error' , UserWarning)
function_with_warnings()

