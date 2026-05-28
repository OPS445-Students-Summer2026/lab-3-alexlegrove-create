#!/usr/bin/env python3

my_list = [ 100, 200, 300, 'six hundred' ]

def give_list():
    return(my_list)

def give_first_item():
    return(str(my_list[0]))

def give_first_and_last_item():
    first = my_list[0]
    last = my_list[-1]
    first_last_list = [first, last]
    return(first_last_list)

def give_second_and_third_item():
    second = my_list[1]
    third = my_list[2]
    second_third_list = [ second, third]
    return(second_third_list)


if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())