import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__
    dir_ = dir(obj)
    obj_attributes = list(filter(lambda i: not callable(getattr(obj, i)) and not i.startswith('__'), dir_))
    obj_methods = list(filter(lambda i: callable(getattr(obj, i)), dir_))
    obj_module = inspect.getmodule(obj)

    info = {
        "type": obj_type,
        "attributes": obj_attributes,
        "methods": obj_methods,
        "module": obj_module
    }
    
    return info


number_info = introspection_info(42)
print(number_info)

class Example:
    def __init__(self, name):
        self.name = name
        self.value = 42

    def greet(self):
        return f"Hello, {self.name}!"

human = Example('Alex')
human_info = introspection_info(human)
print(human_info)

# import requests
# # help(requests.get)
#
# some_string = "I'm string"
# some_number = 42
# some_list = [some_string, some_number]
#
# def some_function(param, param_2='n/a'):
#     print(f'my param is: %{param}, %{param_2}')
#
# class SomeClass:
#     def __init__(self):
#         self.attribute_1 = 27
#
#     def some_class_method(self, value):
#         self.attribute_1 = value
#         print(self.attribute_1)
#
# some_object = SomeClass()