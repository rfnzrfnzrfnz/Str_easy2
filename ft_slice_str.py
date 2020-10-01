def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_slice_str(str, start, end):
    result = ""
    for i in range(start, end + 1):
        if i >= ft_len(str):
            break
        result = result + str[i]
    return result
