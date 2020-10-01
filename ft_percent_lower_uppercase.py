def ft_percent_lower_uppercase(str):
    up = 0
    low = 0
    for i in str:
        if i == i.upper():
            up += 1
        else:
            low += 1
    return up / low * 100
