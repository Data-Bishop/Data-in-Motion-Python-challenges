def Order_List(default_list, order='Asc'):
    order = order.capitalize()
    if order == 'None':
        new_list = default_list
        print(new_list)
    elif order == 'Asc':
        new_list = sorted(default_list, reverse=False)
        print(new_list)
    elif order == 'Des':
        new_list = sorted(default_list, reverse=True)
        print(new_list)
    else :
        print("Please enter either 'none', 'asc', 'desc' as argument. Note 'asc' is set as default")
