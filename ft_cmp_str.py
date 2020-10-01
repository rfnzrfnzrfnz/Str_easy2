def ft_len(str1):
    l = 0
    for i in str1:
        l += 1
    return (l)


def ft_cmp_str(str1, str2, num):
    result = ""
    for i in range(num):
        result = result + str1[i]
    result = result + str2

    for i in range(num, ft_len(str1)):
        result = result + str1[i]
    return result
