def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_first_end_three(str):
    if ft_len(str) > 5:
        return(str[:3] + str[-3:])
    else:
        return(str[0] * ft_len(str))
