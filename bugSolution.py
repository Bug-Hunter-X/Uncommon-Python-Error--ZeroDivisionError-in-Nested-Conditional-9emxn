def function_with_uncommon_error_fixed(a, b):
    if b == 0:
        return float('inf')  # Or raise an exception, or handle it appropriately
    elif a == 0:
        return 0
    else:
        return a / b

result = function_with_uncommon_error_fixed(5, 0) #No Error
print(result) #Output: inf 