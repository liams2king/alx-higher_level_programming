#!/usr/bin/python3
def search_replace(my_list, searching, replaced):
    new_list = list(map(lambda x: replaced if x == searching else x, my_list))
    return (new_list)
