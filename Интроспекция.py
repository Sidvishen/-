def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    module = obj.__class__.__module__
    obj_info = {
        'Тип обекта': obj_type,
        'Атрибут': attributes,
        'Метод': methods,
        'Модуль': module
    }

    return obj_info

number_info = introspection_info(42)
print(number_info)