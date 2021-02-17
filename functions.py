'''transform_to_string that takes a
list as a parameter and returns all its
elements as a string'''


def transform_to_string(datalist: list):
    var_string = ""
    for element in datalist:
        var_string += str(element)
    return var_string


#transform_to_string([1, "hello", True])

'''get_unique_elements that takes a list as parameter 
and return list of only unique elements. '''
# [1, 2, 4]
def get_unique_elements(elements_list: list):
    unique_list = []
    for element in elements_list:

        if element not in unique_list:
            unique_list.append(element)

    return unique_list
#get_unique_elements([1, 1, 2, 4, 4])

# or other way to do get unique elements

def get_unique_elements_2(elements_list: list):
    filtered_elements_list = set(elements_list)
    elements_list = list(filtered_elements_list)
    return elements_list

#get_unique_elements_2([1, 1, 2, 4, 4])

'''break_list_by_value that takes a list as 
a parameter, and another value as second parameter, 
and returns a tuple of the lists divided 
by the first instance of separator, if separator is not in the list 
return the list as tuple, excluding separator. '''

def break_list_by_value(value_list: list, separator: str):
    list_one = []
    list_two = []
    value_tuple = ()
    past_separator = False
    for value in value_list:
        if value != separator:
            if past_separator == True:
                list_two.append(value)
            else:
                list_one.append(value)
        elif value == separator:
            past_separator = True
            continue
    if list_two == []:
        no_separator_tuple = tuple(list_one)
        return no_separator_tuple
    else:
        value_tuple = list(value_tuple)
        value_tuple.append(list_one)
        value_tuple.append(list_two)
        value_tuple = tuple(value_tuple)
        return value_tuple

break_list_by_value([1, 2, "a", True], "a")
# ([1, 2], [True])

break_list_by_value([1, 2, True], "a")
# (1, 2, True)
