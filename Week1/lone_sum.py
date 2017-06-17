def lone_sum(a, b, c):
    all_items = []
    lon_items = []
    all_items.append(a)
    all_items.append(b)
    all_items.append(c)
    for item in all_items:
        if all_items.count(item) == 1:
            lon_items.append(item)
    return sum(lon_items)

print lone_sum(3, 3, 3)