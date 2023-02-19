def Order_List(default_list, order):
    if order == 'none':
        new_list = default_list
        print(new_list)
    elif order == 'asc':
        new_list = default_list.sort(reverse=False)
        print(new_list)
    elif order == 'desc':
        new_list = default_list.sort(reverse=True)
        