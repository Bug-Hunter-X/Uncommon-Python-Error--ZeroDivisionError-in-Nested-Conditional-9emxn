def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  # This is fine
    elif b == 0:
        return 1/b  # ZeroDivisionError
    else:
        return a / b

result = function_with_uncommon_error(5, 0) #Error, ZeroDivisionError
print(result)