def create_an_empty_list():
    return []

def create_a_list():
    return [1,2,3,4]

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    del l[0]
    return l

def retrieve_first_element_from_list(l):
    first_item = l[0]
    return first_item

def retrieve_element_from_index(l, index):
    element = l[index]
    return element

def retrieve_last_element_from_list(l):
    last_item = l[-1]
    return last_item
