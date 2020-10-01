def ft_len(str2):
    l = 0
    for i in str2:
        l += 1
    return (l)


def ft_find_str(str1, str2):
    for i in range(len(str1)):
        flag = 0
        for j in range(ft_len(str2)):
            if str1[i + j] != str2[j]:
                flag = 1
        if flag == 0:
            return i
    return -1
