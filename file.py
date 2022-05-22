def greeter(func):
    def inner(*args, **kwargs):
        val = func(*args, **kwargs)
        return "Aloha " + val.title()
    return inner


def sums_of_str_elements_are_equal(func):
    def inner(*args, **kwargs):
        val = func(*args, **kwargs).split()
        first_number, second_number = val[0], val[1]
        first_number_sum, second_number_sum = 0, 0
        
        for i in range(1, len(first_number)):
            first_number_sum += int(first_number[i])
        if first_number[0] == '-':
            first_number_sum *= (-1)
        else:
            first_number_sum += int(first_number[0])

        for i in range(1, len(second_number)):
            second_number_sum += int(second_number[i])
        if second_number[0] == '-':
            second_number_sum *= (-1)
        else:
            second_number_sum += int(second_number[0])
        
        return f"{first_number_sum} == {second_number_sum}" if first_number_sum == second_number_sum else f"{first_number_sum} != {second_number_sum}"

    return inner


def format_output(*required_keys):
    def wrapper(func):
        def inner(*args):
            input_dict = func(*args)
            formated_dict = {}
            for key in required_keys:
                value_list = []
                for k in key.split("__"):
                    if k not in input_dict:
                        raise ValueError
                    current_value = input_dict[k]
                    if current_value:
                        value_list.append(current_value)
                    else:
                        value_list.append("Empty value")
                formated_dict[key] = " ".join(value_list)
            return formated_dict
        return inner
    return wrapper


def add_method_to_instance(klass):
    def wrapper(func):
        def inner(self):
            return func()
        setattr(klass, func.__name__, inner)
        return func
    return wrapper