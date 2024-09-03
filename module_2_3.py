my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

l = len(my_list)
p = 0

while p < l:
    if my_list[p] == 0:
        p = p + 1
    elif my_list[p] > 0:
        print(my_list[p])
        p = p + 1
        continue
    else:
        break
