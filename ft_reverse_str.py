def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_reverse_str(str):
    a = ''
    for i in range(-1, -ft_len(str) - 1, -1):
        a += str[i]
    return a
