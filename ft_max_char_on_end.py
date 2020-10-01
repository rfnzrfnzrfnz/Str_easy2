def ft_max_char_on_end(str):
    digits = "0123456789"

    temp = ""
    result = ""
    for char in str:
        if char in digits:
            temp = temp + char
        else:
            if len(temp) > len(result):
                result = temp
                temp = ""
    if len(temp) > len(result):
        result = temp
    return result