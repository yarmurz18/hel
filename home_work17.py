def check_number_decorator(func):
    def check(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(*args) is int:
            new_result = result + 10
        else:
            new_result = result
        return  new_result
    return check

@check_number_decorator
def get_number(num):
    return num
num = 35
print(get_number(num))

