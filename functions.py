# TODO: Implement the following functions based on the descriptions.

element = 2
dct= {'a': 1, 'b': 2, 'c': 1}
value = 1



def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    lst = [1,2,3]
    print(lst.reverse())
    return lst.reverse()
    
  

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    
    element_count = 0
    for item in lst:
        if element == item:
            element_count += 1
            print(f"Element occurs {element_count} times")

    return element_count
    

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    list = []
    for key in dct:
        if value == dct[key]:
            list.append(key)
        
    print(list)
    return list
    

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    # lst1 = [1, 3, 5]
    # lst2 = [2, 4, 6]
    
    # sort1 = lst1.sort()
    # sort2 = lst2.sort()
    # merged = sort1 + sort2
    # # print(f"{sort1} + {sort2}")
    # return merged
    pass


def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    pass  # Implement this

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    str1 = "hello"
    str2 = "world"
    

    if list(str1).sort() == list(str2).sort():
        print('True')
        return True
    else:
        print('False')
        return False
    


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    # nested_list = [[1, 2], [3, 4]]
    flattened = list(zip(*nested_list))
    print(flattened)


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    lst = [1, 2, 2, 3, 3]
    count = 0 
    print(lst)
    for item in lst:
        if item:
            count += 1

            if count > 1:
                print(item)
                lst.remove(item)
    print(lst)
    return lst


def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    lst1 = [1, 2, 3] 
    lst2 = [3, 4, 5]

    for i in lst1:
        for j in lst2:
            if i in lst2 and j in lst1:
                print(i)
    return i
lst = [1, 2, 3]
reverse_list(lst)
# element = input("Element:")
count_occurrences(lst, element)
get_keys_with_value(dct, value)

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merge_sorted_lists(lst1, lst2)

str1 = "hello"
str2 = "world"
is_anagram(str1, str2)
find_common_elements(lst1, lst2)
nested_list = [[1, 2], [3, 4]]
flatten_list(nested_list)

lst = [1, 2, 2, 3, 3]
remove_duplicates(lst)