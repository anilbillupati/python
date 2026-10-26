
from typing import List

test_list=[12,34,56,87,45,23,21,21,12,21,21,21,12]
def create_set_from_list(list:List[int])->set:
    my_Set={}
    for element in list:
        my_Set.add(element)
    return my_Set


print(create_set_from_list(test_list))

